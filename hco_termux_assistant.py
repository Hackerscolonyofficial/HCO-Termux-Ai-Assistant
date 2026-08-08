#!/usr/bin/env python3
"""HCO Termux AI Security Assistant - Code by Azhar HCO Team."""

import os, re, json, shutil, socket, subprocess, platform, datetime, time, webbrowser

RESET="\033[0m"; BOLD="\033[1m"
RED="\033[91m"; GREEN="\033[92m"; YELLOW="\033[93m"
BLUE="\033[94m"; MAGENTA="\033[95m"; CYAN="\033[96m"; WHITE="\033[97m"

YOUTUBE_URL="https://youtube.com/@hackers_colony_tech?si=5hYoJ43YgPJ5rzNJ"
REPORT_DIR=os.path.expanduser("~/hco_reports")

def c(text,color=WHITE,bold=False):
    return color+(BOLD if bold else "")+str(text)+RESET

def clear_screen():
    os.system("clear" if os.name!="nt" else "cls")

def exists(cmd): return shutil.which(cmd) is not None

def run(cmd,timeout=5):
    try:
        r=subprocess.run(cmd,shell=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,timeout=timeout)
        return r.stdout.strip()
    except Exception: return ""

def banner():
    clear_screen()
    art=[
        "##   ##   ####    ###",
        "##   ##  ##      ## ##",
        "#######  ##      ## ##",
        "##   ##  ##      ## ##",
        "##   ##   ####    ###",
    ]
    colors=[CYAN,BLUE,MAGENTA,CYAN,BLUE]
    for i,line in enumerate(art):
        print(c(line.center(42),colors[i],True))
    print()
    print(c("HCO TERMUX AI SECURITY ASSISTANT",WHITE,True))
    print(c("Termux AI Security Assistant by Azhar HCO Team",MAGENTA,True))
    print()

def support():
    print(c("╔"+"═"*66+"╗",MAGENTA))
    print(c("║  THIS IS A PREMIUM-STYLE TOOL",YELLOW,True))
    print(c("║  BUT WE ARE PROVIDING IT FOR FREE.",YELLOW,True))
    print(c("║",MAGENTA))
    print(c("║  Local Android + Termux security diagnostics",WHITE))
    print(c("║  No root • No exploit / attack functions",GREEN))
    print(c("╚"+"═"*66+"╝",MAGENTA))
    print()
    print(c("This is a premium-style tool, but we are providing it for free.",YELLOW,True))
    print("We are redirecting you to our YouTube channel if you would like")
    print("to support us.")
    print(c("Please subscribe and turn on the bell if you enjoy our content.",CYAN))
    print()

def open_youtube():
    print(c("Opening YouTube app...",GREEN,True))
    opened=False
    if exists("am"):
        try:
            subprocess.Popen(["am","start","-a","android.intent.action.VIEW","-d",YOUTUBE_URL],
                             stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            opened=True
        except Exception: pass
    if not opened:
        try: opened=webbrowser.open(YOUTUBE_URL)
        except Exception: pass
    if not opened:
        print(c("Could not open YouTube automatically.",YELLOW))
        print(YOUTUBE_URL)
    print()
    input(c("Press ENTER to start HCO Termux Assistant...",CYAN))

def android_info():
    if exists("getprop"):
        return {
            "Android":run("getprop ro.build.version.release") or "Unknown",
            "Device":(run("getprop ro.product.manufacturer")+" "+run("getprop ro.product.model")).strip() or "Unknown",
            "Security Patch":run("getprop ro.build.version.security_patch") or "Unknown"
        }
    return {"Android":"Not detected","Device":platform.node() or "Unknown","Security Patch":"N/A"}

def ram():
    try:
        d={}
        for line in open("/proc/meminfo",encoding="utf-8",errors="ignore"):
            if line.startswith(("MemTotal:","MemAvailable:")):
                d[line.split(":")[0]]=int(re.findall(r"\d+",line)[0])
        total=d.get("MemTotal",0)/1024/1024
        avail=d.get("MemAvailable",0)/1024/1024
        return f"{total:.1f} GB total / {avail:.1f} GB available" if total else "Unknown"
    except Exception: return "Unknown"

def storage():
    try:
        t,u,f=shutil.disk_usage(os.path.expanduser("~"))
        return f"{f/1024**3:.1f} GB free / {t/1024**3:.1f} GB"
    except Exception: return "Unknown"

def local_ip():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM); s.settimeout(1)
        s.connect(("1.1.1.1",80)); ip=s.getsockname()[0]; s.close(); return ip
    except Exception:
        try: return socket.gethostbyname(socket.gethostname())
        except Exception: return "Unknown"

def dns():
    vals=[]
    if exists("getprop"):
        for line in run("getprop").splitlines():
            if "net.dns" in line:
                m=re.search(r"\[\s*([0-9a-fA-F:.]+)\s*\]",line)
                if m: vals.append(m.group(1))
    try:
        for line in open("/etc/resolv.conf",encoding="utf-8",errors="ignore"):
            if line.strip().startswith("nameserver"):
                parts=line.split()
                if len(parts)>1: vals.append(parts[1])
    except Exception: pass
    return ", ".join(dict.fromkeys(vals)) or "Unknown"

def ssh():
    installed=exists("ssh") or exists("sshd")
    running=bool(run("pgrep -a sshd"))
    if running: return "Running: sshd"
    if installed: return "Installed: OpenSSH"
    return "Not detected"

def packages():
    if exists("dpkg"):
        out=run("dpkg-query -W -f='${binary:Package}\\n' 2>/dev/null")
        n=len([x for x in out.splitlines() if x.strip()])
        return f"{n} installed packages" if n else "Unknown"
    return "Unknown"

def scan():
    a=android_info(); s=ssh(); d=dns(); ip=local_ip()
    findings=[]; score=100
    if s.startswith("Running"):
        score-=15
        findings.append(("MEDIUM","SSH-related service detected",
            "If you do not need remote access: run `pkill sshd`. If you never use OpenSSH, run `pkg uninstall openssh`. If you use SSH, keep it and start it only when needed."))
    elif s.startswith("Installed"):
        score-=5
        findings.append(("LOW","OpenSSH is installed",
            "If you do not use SSH, consider `pkg uninstall openssh`. Otherwise no action is required."))
    if d=="Unknown":
        score-=2
        findings.append(("LOW","DNS configuration could not be read",
            "If internet works normally this may be informational. Otherwise check Android network settings or `/etc/resolv.conf`."))
    if ip=="Unknown":
        score-=2
        findings.append(("LOW","Local IP could not be detected","Check your network and run `ip addr`."))
    rating="GOOD" if score>=90 else "MODERATE" if score>=75 else "NEEDS ATTENTION" if score>=50 else "HIGH ATTENTION"
    return {
        "timestamp":datetime.datetime.now().isoformat(timespec="seconds"),
        "android":a,"device":a.get("Device","Unknown"),"termux":os.environ.get("PREFIX","Not detected"),
        "ram":ram(),"storage":storage(),"local_ip":ip,"dns":d,"ssh":s,"packages":packages(),
        "permissions":"Review Termux:API / storage permissions and grant only what you need",
        "security_score":score,"rating":rating,
        "findings":[{"severity":x[0],"title":x[1],"action":x[2]} for x in findings]
    }

def print_scan(r):
    print(c("Running local security diagnostics...",CYAN,True)); print()
    rows=[("Android",r["android"].get("Android","Unknown")),("Device",r["device"]),
          ("Termux",r["termux"]),("RAM",r["ram"]),("Storage",r["storage"]),
          ("Local IP",r["local_ip"]),("DNS",r["dns"]),("SSH",r["ssh"]),
          ("Packages",r["packages"]),("Permissions",r["permissions"])]
    for k,v in rows:
        ok=v not in ("Unknown","Not detected")
        print(c(("✓ " if ok else "⚠ ")+f"{k:<12} {v}",GREEN if ok else YELLOW))
    print()
    print(c("╔"+"═"*48+"╗",YELLOW)); print(c("║  SECURITY SCORE",YELLOW,True))
    print(c("║",YELLOW)); print(c(f"║  {r['security_score']:>3}/100 • {r['rating']}",YELLOW,True))
    print(c("╚"+"═"*48+"╝",YELLOW)); print()
    print(c("Findings & recommendations",MAGENTA,True)); print()
    if not r["findings"]: print(c("✓ No basic issues were detected by this scan.",GREEN))
    for f in r["findings"]:
        col=RED if f["severity"]=="HIGH" else YELLOW if f["severity"]=="MEDIUM" else CYAN
        print(c(f"[{f['severity']}] {f['title']}",col,True)); print("→ "+f["action"]); print()

def save_report(r):
    os.makedirs(REPORT_DIR,exist_ok=True)
    path=os.path.join(REPORT_DIR,"security_report_"+datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+".json")
    try:
        with open(path,"w",encoding="utf-8") as f: json.dump(r,f,indent=2,ensure_ascii=False)
        print(c("Report saved: "+path,GREEN))
    except Exception as e: print(c("Could not save report: "+str(e),RED))

def network():
    print(c("NETWORK DIAGNOSTICS",CYAN,True)); print()
    print("Local IP:",local_ip()); print("DNS:     ",dns()); print()
    out=run("ss -lntup") if exists("ss") else run("netstat -lntup") if exists("netstat") else ""
    print(c("Local listening sockets:",YELLOW,True) if out else c("No local socket information is available.",YELLOW))
    if out: print(out)
    input(c("\nPress ENTER to continue...",CYAN))

def privacy():
    print(c("PRIVACY CHECK",MAGENTA,True)); print()
    for k,v in [("Public IP lookup","Not performed"),("External host scanning","Disabled"),
                ("Password collection","Disabled"),("Credential extraction","Disabled"),("Local report","Enabled")]:
        print(c(f"✓ {k:<25} {v}",GREEN))
    print("\nThis tool is designed to inspect your own device.")
    input(c("\nPress ENTER to continue...",CYAN))

def health():
    print(c("TERMUX / LINUX HEALTH CHECK",GREEN,True)); print()
    for name,ok in [("Python",exists("python") or exists("python3")),("Git",exists("git")),
                    ("curl",exists("curl")),("ip",exists("ip")),("ss",exists("ss")),("pkg",exists("pkg"))]:
        print(c(f"{'✓' if ok else '⚠'} {name:<10} {'Available' if ok else 'Not detected'}",GREEN if ok else YELLOW))
    input(c("\nPress ENTER to continue...",CYAN))

def assistant():
    print(c("LOCAL SECURITY ASSISTANT",BLUE,True))
    print("Ask about the latest scan. Type 'back' to return.\n")
    r=scan()
    while True:
        try: q=input(c("HCO AI > ",CYAN,True)).strip().lower()
        except (EOFError,KeyboardInterrupt): return
        if q=="back": return
        if "score" in q:
            print(c(f"Current rule-based score: {r['security_score']}/100 ({r['rating']}).",GREEN))
        elif "ssh" in q:
            print(c(f"SSH status: {r['ssh']}. If unused, stop it with `pkill sshd`.",YELLOW))
        elif "dns" in q: print("Detected DNS:",r["dns"])
        elif "network" in q: print("Local IP:",r["local_ip"])
        elif "secure" in q or "phone" in q:
            print(c("This tool cannot guarantee device security. Review every finding before acting.",YELLOW))
        elif q=="help":
            print("Try: security score | check SSH | what is DNS? | check my network | check my phone")
        else:
            print("Try: security score | check SSH | what is DNS? | check my network | check my phone")
        print()

def full_scan():
    banner(); r=scan(); print_scan(r); save_report(r)
    input(c("\nPress ENTER to continue...",CYAN))

def menu():
    while True:
        banner()
        print(c("╔════════════════════════════════════════════╗",CYAN))
        print(c("║              MAIN MENU                    ║",CYAN,True))
        print(c("╠════════════════════════════════════════════╣",CYAN))
        for line in ["║  [1] Full Security Scan                  ║","║  [2] Network Diagnostics                 ║",
                     "║  [3] Privacy Check                       ║","║  [4] Termux / Linux Health               ║",
                     "║  [5] Local Security Assistant            ║","║  [6] Open Hackers Colony YouTube         ║",
                     "║  [0] Exit                                ║"]:
            print(c(line,WHITE))
        print(c("╚════════════════════════════════════════════╝",CYAN)); print()
        try: choice=input(c("HCO@termux > ",MAGENTA,True)).strip()
        except (EOFError,KeyboardInterrupt): return
        if choice=="1": full_scan()
        elif choice=="2": banner(); network()
        elif choice=="3": banner(); privacy()
        elif choice=="4": banner(); health()
        elif choice=="5": banner(); assistant()
        elif choice=="6": open_youtube()
        elif choice=="0": print(c("Thank you for using HCO Termux AI Security Assistant.",GREEN)); return
        else: print(c("Invalid option. Choose 0-6.",YELLOW)); time.sleep(1)

def main():
    banner(); support()
    for n in (3,2,1):
        print(c(f"Opening YouTube in {n}...",YELLOW,True)); time.sleep(1)
    open_youtube()
    menu()

if __name__=="__main__":
    main()
