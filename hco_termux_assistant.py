#!/data/data/com.termux/files/usr/bin/python
# HCO Termux Assistant
# Termux AI Security Assistant by Hackers Colony
# Safe/local security diagnostics for the user's own Android/Termux environment.

import json
import os
import platform
import re
import shutil
import socket
import subprocess
import sys
import time
from datetime import datetime

# -----------------------------
# Configuration
# -----------------------------
CHANNEL_URL = os.environ.get(
    "HCO_YOUTUBE_URL",
    "https://youtu.be/8vSOT11exyM?si=84dSfRgOQUxxDOmb"
)

# ANSI colors
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

CLEAR = "\033[2J\033[H"


def c(text, color):
    return f"{color}{text}{RESET}"


def run_cmd(cmd, timeout=5):
    try:
        p = subprocess.run(
            cmd,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=timeout,
        )
        return p.stdout.strip()
    except Exception:
        return ""


def command_exists(name):
    return shutil.which(name) is not None


def clear_screen():
    print(CLEAR, end="")


def pause(msg="Press ENTER to continue..."):
    input(c(f"\n{msg}", CYAN))


def box(lines, color=CYAN, width=68):
    print(c("╔" + "═" * width + "╗", color))

    for line in lines:
        clean = re.sub(r"\x1b\[[0-9;]*m", "", line)
        pad = max(0, width - len(clean))

        print(
            c("║", color)
            + line
            + " " * pad
            + c("║", color)
        )

    print(c("╚" + "═" * width + "╝", color))


def banner():
    clear_screen()

    art = [
        ██╗  ██╗ ██████╗ ██████╗ 
██║  ██║██╔════╝██╔═══██╗
███████║██║     ██║   ██║
██╔══██║██║     ██║   ██║
██║  ██║╚██████╗╚██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
    ]

    for i, line in enumerate(art):
        print(
            c(
                line,
                [CYAN, BLUE, MAGENTA, CYAN, BLUE, MAGENTA][i]
            )
        )

    print()

    print(
        c(
            "HCO TERMUX AI SECURITY ASSISTANT",
            BOLD + WHITE
        )
    )

    print(
        c(
            "Termux AI Security Assistant by Azhar HCO Team",
            BOLD + MAGENTA
        )
    )

    print()

    box(
        [
            c(
                "THIS IS A PREMIUM TOOL,",
                BOLD + YELLOW
            ),
            c(
                "BUT WE ARE PROVIDING IT FOR FREE.",
                BOLD + YELLOW
            ),
            c(
                "Local Android + Termux security diagnostics",
                WHITE
            ),
            c(
                "No root • No exploit / attack functions",
                GREEN
            ),
        ],
        MAGENTA,
        width=58,
    )


def shlex_quote(s):
    return "'" + s.replace("'", "'\\''") + "'"


def open_youtube():
    """
    Open the supplied YouTube URL.

    First try the YouTube Android app explicitly.
    If that fails, fall back to Android's normal VIEW handler.
    """

    if not command_exists("am"):
        return False

    url = shlex_quote(CHANNEL_URL)

    # Prefer YouTube Android app.
    app_cmd = (
        "am start -a android.intent.action.VIEW "
        f"-d {url} "
        "-p com.google.android.youtube "
        ">/dev/null 2>&1"
    )

    result = subprocess.run(
        app_cmd,
        shell=True
    ).returncode

    if result == 0:
        return True

    # Fallback to Android's normal URL handler.
    fallback = (
        "am start -a android.intent.action.VIEW "
        f"-d {url} "
        ">/dev/null 2>&1"
    )

    return (
        subprocess.run(
            fallback,
            shell=True
        ).returncode == 0
    )


def startup_redirect():
    """
    Startup presentation flow.

    Shows HCO branding, support message,
    9-to-0 countdown, opens YouTube,
    then waits for user to return to Termux.
    """

    banner()

    print()

    print(
        c(
            "This is a premium tool, but we are providing it for free.",
            BOLD + YELLOW
        )
    )

    print(
        c(
            "We are redirecting you to our YouTube channel if you would like to support us.",
            WHITE
        )
    )

    print(
        c(
            "Please subscribe and turn on the bell if you enjoy our content.",
            CYAN
        )
    )

    print()

    for n in range(9, -1, -1):

        print(
            "\r"
            + c(
                "Opening YouTube in ",
                YELLOW
            )
            + c(
                str(n),
                BOLD + WHITE
            )
            + "   ",
            end="",
            flush=True,
        )

        time.sleep(0.45)

    print("\n")

    print(
        c(
            "Opening YouTube app...",
            BOLD + GREEN
        )
    )

    opened = open_youtube()

    if not opened:

        print(
            c(
                "YouTube app could not be opened automatically.",
                YELLOW
            )
        )

        print(
            c(
                "Open this link manually:",
                WHITE
            )
        )

        print(
            c(
                CHANNEL_URL,
                CYAN
            )
        )

    print()

    print(
        c(
            "After supporting Hackers Colony, return to Termux.",
            BOLD + WHITE
        )
    )

    pause(
        "Press ENTER to start HCO Termux Assistant..."
    )


def get_android_version():

    return (
        run_cmd(
            "getprop ro.build.version.release"
        )
        or "Unknown"
    )


def get_device():

    model = (
        run_cmd(
            "getprop ro.product.model"
        )
        or platform.machine()
    )

    brand = run_cmd(
        "getprop ro.product.brand"
    )

    return f"{brand} {model}".strip()


def get_termux_version():

    out = run_cmd(
        "termux-info",
        timeout=8
    )

    if not out:
        return "Unknown"

    m = re.search(
        r"Termux version:\s*([^\n]+)",
        out
    )

    return (
        m.group(1).strip()
        if m
        else "Detected"
    )


def get_ram():

    out = run_cmd(
        "cat /proc/meminfo"
    )

    m = re.search(
        r"MemTotal:\s+(\d+)\s+kB",
        out
    )

    if not m:
        return "Unknown"

    gb = int(m.group(1)) / 1024 / 1024

    return f"{gb:.1f} GB"


def get_storage():

    try:

        total, used, free = shutil.disk_usage(
            os.path.expanduser("~")
        )

        return (
            f"{free / (1024**3):.1f} GB free / "
            f"{total / (1024**3):.1f} GB"
        )

    except Exception:

        return "Unknown"


def get_local_ip():

    try:

        s = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )

        s.settimeout(1)

        s.connect(
            ("1.1.1.1", 80)
        )

        ip = s.getsockname()[0]

        s.close()

        return ip

    except Exception:

        return "Unavailable"


def get_dns():

    # First try /etc/resolv.conf.
    resolv = run_cmd(
        "cat /etc/resolv.conf"
    )

    servers = re.findall(
        r"nameserver\s+([0-9a-fA-F:.\-]+)",
        resolv
    )

    # Android may expose DNS through getprop.
    if not servers:

        props = run_cmd(
            "getprop 2>/dev/null"
        )

        servers = re.findall(
            r"\[net\.dns\d*\]: \[([^\]]+)\]",
            props
        )

    return (
        ", ".join(
            dict.fromkeys(
                servers[:4]
            )
        )
        if servers
        else "Unknown"
    )


def get_interfaces():

    out = run_cmd(
        "ip -brief addr 2>/dev/null"
    )

    return (
        out
        or "Unavailable"
    )


def get_open_listeners():

    # Only checks local listening sockets.
    # It does not scan external hosts.

    out = run_cmd(
        "ss -lntup 2>/dev/null",
        timeout=5
    )

    if not out:

        out = run_cmd(
            "netstat -lntup 2>/dev/null",
            timeout=5
        )

    return (
        out
        or "No socket information available"
    )


def get_ssh_status():

    candidates = [
        "sshd",
        "dropbear"
    ]

    found = [
        name
        for name in candidates
        if command_exists(name)
    ]

    running = run_cmd(
        "pgrep -a sshd 2>/dev/null"
    )

    if not found:

        return "Not detected"

    if running:

        return (
            "Installed + RUNNING: "
            + ", ".join(found)
        )

    return (
        "Installed, not detected running: "
        + ", ".join(found)
    )


def package_update_check():

    if not command_exists("pkg"):

        return "pkg command unavailable"

    out = run_cmd(
        "pkg list-installed 2>/dev/null | wc -l",
        timeout=8
    )

    return (
        f"{out.strip() or 'Unknown'} "
        "installed packages"
    )


def permission_note():

    return (
        "Review Termux:API / storage permissions "
        "and only grant what you need"
    )


def analyze(data):

    findings = []

    score = 100

    # SSH running.
    if data["ssh_status"].startswith(
        "Installed + RUNNING"
    ):

        findings.append(
            (
                "MEDIUM",
                "SSH server is installed and appears to be running.",
                "If you do NOT use SSH: run `pkill sshd`, "
                "then `pkg uninstall openssh`. "
                "If you DO use SSH, keep it and only start it when needed."
            )
        )

        score -= 17

    # SSH installed but not running.
    elif data["ssh_status"].startswith(
        "Installed"
    ):

        findings.append(
            (
                "LOW",
                "OpenSSH is installed, but sshd is not detected as running.",
                "If you never use SSH: run `pkg uninstall openssh`. "
                "If you use it, no action is required."
            )
        )

        score -= 12

    # DNS.
    if data["dns"] == "Unknown":

        findings.append(
            (
                "LOW",
                "DNS servers could not be read from Android/Termux.",
                "Run `getprop | grep -E 'net\\.dns'` "
                "to view Android DNS values. "
                "If DNS works normally, this is an information-only warning."
            )
        )

        score -= 5

    # Socket information.
    if (
        "No socket information"
        in data["listeners"]
    ):

        findings.append(
            (
                "LOW",
                "Local listening-socket information is unavailable.",
                "Install the required tools with "
                "`pkg install iproute2 net-tools`, "
                "then run the scan again."
            )
        )

        score -= 3

    if score >= 90:

        level = "GOOD"

    elif score >= 75:

        level = "MODERATE"

    elif score >= 50:

        level = "NEEDS ATTENTION"

    else:

        level = "HIGH ATTENTION"

    return (
        max(0, score),
        level,
        findings
    )


def collect_scan():

    data = {

        "timestamp":
            datetime.now().isoformat(
                timespec="seconds"
            ),

        "device":
            get_device(),

        "android":
            get_android_version(),

        "termux":
            get_termux_version(),

        "ram":
            get_ram(),

        "storage":
            get_storage(),

        "local_ip":
            get_local_ip(),

        "dns":
            get_dns(),

        "interfaces":
            get_interfaces(),

        "listeners":
            get_open_listeners(),

        "ssh_status":
            get_ssh_status(),

        "packages":
            package_update_check(),

        "permissions":
            permission_note(),
    }

    score, level, findings = analyze(
        data
    )

    data["score"] = score

    data["level"] = level

    data["findings"] = findings

    return data


def print_status(
    label,
    value,
    good=True
):

    symbol = "✓" if good else "⚠"

    color = (
        GREEN
        if good
        else YELLOW
    )

    print(
        f"  "
        f"{c(symbol, BOLD + color)} "
        f"{c(label.ljust(22), WHITE)} "
        f"{value}"
    )


def full_scan():

    clear_screen()

    banner()

    print(
        c(
            "\nRunning local security diagnostics...\n",
            BOLD + CYAN
        )
    )

    data = collect_scan()

    print_status(
        "Android",
        data["android"]
    )

    print_status(
        "Device",
        data["device"]
    )

    print_status(
        "Termux",
        data["termux"]
    )

    print_status(
        "RAM",
        data["ram"]
    )

    print_status(
        "Storage",
        data["storage"]
    )

    print_status(
        "Local IP",
        data["local_ip"]
    )

    print_status(
        "DNS",
        data["dns"],
        data["dns"] != "Unknown"
    )

    print_status(
        "SSH",
        data["ssh_status"],
        not data["ssh_status"].startswith(
            "Installed + RUNNING"
        )
    )

    print_status(
        "Packages",
        data["packages"]
    )

    print_status(
        "Permissions",
        data["permissions"]
    )

    score_color = (
        GREEN
        if data["score"] >= 90
        else YELLOW
        if data["score"] >= 75
        else RED
    )

    print()

    box(
        [
            c(
                "SECURITY SCORE",
                BOLD + WHITE
            ),
            c(
                f"{data['score']}/100  •  {data['level']}",
                BOLD + score_color
            ),
        ],
        score_color
    )

    print(
        c(
            "\nWhat needs attention",
            BOLD + MAGENTA
        )
    )

    if data["findings"]:

        print(
            c(
                "The items below include exact commands or actions.",
                DIM
            )
        )

    else:

        print(
            c(
                "No rule-based warnings were detected.",
                GREEN
            )
        )

    print(
        c(
            "\nDetailed findings & fixes",
            BOLD + MAGENTA
        )
    )

    if not data["findings"]:

        print(
            c(
                "✓ No rule-based warnings were detected.",
                GREEN
            )
        )

    else:

        for severity, finding, fix in data["findings"]:

            sev_color = (
                RED
                if severity == "HIGH"
                else YELLOW
            )

            print(
                c(
                    f"\n[{severity}] {finding}",
                    BOLD + sev_color
                )
            )

            import textwrap

            for line in textwrap.wrap(
                fix,
                width=64
            ):

                print(
                    c(
                        f"  FIX: {line}",
                        WHITE
                    )
                )

    # Save JSON report.
    report_dir = os.path.expanduser(
        "~/hco_reports"
    )

    os.makedirs(
        report_dir,
        exist_ok=True
    )

    report_path = os.path.join(
        report_dir,
        "security_report_"
        + datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )
        + ".json"
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=2
        )

    print(
        c(
            f"\nReport saved: {report_path}",
            DIM
        )
    )

    pause()


def network_check():

    clear_screen()

    banner()

    print(
        c(
            "\nNETWORK DIAGNOSTICS\n",
            BOLD + CYAN
        )
    )

    print_status(
        "Local IP",
        get_local_ip()
    )

    print_status(
        "DNS",
        get_dns()
    )

    print(
        c(
            "\nInterfaces:",
            BOLD + WHITE
        )
    )

    print(
        get_interfaces()[:3000]
    )

    print(
        c(
            "\nLocal listening sockets:",
            BOLD + WHITE
        )
    )

    print(
        get_open_listeners()[:5000]
    )

    print(
        c(
            "\nThis module checks only the current device.",
            DIM
        )
    )

    pause()


def privacy_check():

    clear_screen()

    banner()

    print(
        c(
            "\nPRIVACY CHECK\n",
            BOLD + CYAN
        )
    )

    checks = [

        (
            "Public IP lookup",
            "Not performed"
        ),

        (
            "External host scanning",
            "Disabled"
        ),

        (
            "Password collection",
            "Disabled"
        ),

        (
            "Credential extraction",
            "Disabled"
        ),

        (
            "Local report",
            "Enabled"
        ),
    ]

    for label, value in checks:

        print_status(
            label,
            value,
            value in (
                "Not performed",
                "Disabled",
                "Enabled"
            )
        )

    print(
        c(
            "\nPrivacy principle:",
            BOLD + MAGENTA
        )
    )

    print(
        c(
            "HCO Termux Assistant is designed "
            "to inspect your own device and local configuration.",
            WHITE
        )
    )

    pause()


def termux_health():

    clear_screen()

    banner()

    print(
        c(
            "\nTERMUX HEALTH\n",
            BOLD + CYAN
        )
    )

    checks = [

        (
            "Python",
            sys.version.split()[0]
        ),

        (
            "pkg",
            "Available"
            if command_exists("pkg")
            else "Not found"
        ),

        (
            "git",
            "Available"
            if command_exists("git")
            else "Not found"
        ),

        (
            "curl",
            "Available"
            if command_exists("curl")
            else "Not found"
        ),

        (
            "ip",
            "Available"
            if command_exists("ip")
            else "Not found"
        ),

        (
            "ss",
            "Available"
            if command_exists("ss")
            else "Not found"
        ),

        (
            "Storage",
            get_storage()
        ),
    ]

    for label, value in checks:

        print_status(
            label,
            value,
            not value.startswith(
                "Not"
            )
        )

    pause()


def ask_assistant():

    clear_screen()

    banner()

    print(
        c(
            "\nLOCAL SECURITY ASSISTANT\n",
            BOLD + CYAN
        )
    )

    print(
        c(
            "Ask about the latest local scan. "
            "Type 'back' to return.\n",
            DIM
        )
    )

    data = collect_scan()

    while True:

        q = input(
            c(
                "You > ",
                BOLD + MAGENTA
            )
        ).strip().lower()

        if q in (
            "back",
            "exit",
            "quit"
        ):

            return

        if not q:

            continue

        if (
            "score" in q
            or "secure" in q
            or "security" in q
        ):

            print(
                c(
                    f"\nAssistant > "
                    f"Your current rule-based security "
                    f"score is {data['score']}/100 "
                    f"({data['level']}).",
                    GREEN
                )
            )

            if data["findings"]:

                print(
                    c(
                        "Assistant > Main items to review:",
                        WHITE
                    )
                )

                for (
                    sev,
                    finding,
                    fix
                ) in data["findings"]:

                    print(
                        c(
                            f"  • {finding} — {fix}",
                            WHITE
                        )
                    )

            else:

                print(
                    c(
                        "Assistant > "
                        "No rule-based warnings were detected.",
                        GREEN
                    )
                )

        elif "ssh" in q:

            print(
                c(
                    f"\nAssistant > "
                    f"{data['ssh_status']}",
                    WHITE
                )
            )

            print(
                c(
                    "If you do not use SSH/remote access, "
                    "disable or remove unused SSH services.",
                    YELLOW
                )
            )

        elif "dns" in q:

            print(
                c(
                    f"\nAssistant > "
                    f"Detected DNS: {data['dns']}",
                    WHITE
                )
            )

            print(
                c(
                    "DNS translates domain names into IP addresses. "
                    "Review it if you suspect network misconfiguration.",
                    WHITE
                )
            )

        elif (
            "ip" in q
            or "network" in q
        ):

            print(
                c(
                    f"\nAssistant > "
                    f"Local IP: {data['local_ip']}",
                    WHITE
                )
            )

            print(
                c(
                    "I only inspect the current device's "
                    "local network information.",
                    DIM
                )
            )

        elif (
            "android" in q
            or "phone" in q
            or "device" in q
        ):

            print(
                c(
                    f"\nAssistant > "
                    f"Device: {data['device']} | "
                    f"Android: {data['android']}",
                    WHITE
                )
            )

        elif "help" in q:

            print(
                c(
                    "\nAssistant > Try: "
                    "'security score', 'SSH', 'DNS', "
                    "'network', 'phone', or 'help'.",
                    WHITE
                )
            )

        else:

            print(
                c(
                    "\nAssistant > "
                    "I can explain the local checks, "
                    "but I cannot verify every Android "
                    "security property without privileged access.",
                    YELLOW
                )
            )


def menu():

    while True:

        clear_screen()

        banner()

        print()

        options = [

            (
                "1",
                "Full Security Scan"
            ),

            (
                "2",
                "Network Diagnostics"
            ),

            (
                "3",
                "Privacy Check"
            ),

            (
                "4",
                "Termux Health"
            ),

            (
                "5",
                "Security Assistant"
            ),

            (
                "6",
                "Open Hackers Colony YouTube"
            ),

            (
                "0",
                "Exit"
            ),
        ]

        for num, title in options:

            print(
                f"  "
                f"{c('[' + num + ']', BOLD + CYAN)} "
                f"{c(title, WHITE)}"
            )

        print()

        choice = input(
            c(
                "HCO > ",
                BOLD + MAGENTA
            )
        ).strip()

        if choice == "1":

            full_scan()

        elif choice == "2":

            network_check()

        elif choice == "3":

            privacy_check()

        elif choice == "4":

            termux_health()

        elif choice == "5":

            ask_assistant()

        elif choice == "6":

            startup_redirect()

        elif choice == "0":

            print(
                c(
                    "\nStay ethical. Stay curious. "
                    "— Hackers Colony\n",
                    BOLD + CYAN
                )
            )

            break

        else:

            print(
                c(
                    "Invalid option.",
                    RED
                )
            )

            time.sleep(1)


if __name__ == "__main__":

    try:

        startup_redirect()

        menu()

    except KeyboardInterrupt:

        print(
            c(
                "\n\nExiting HCO Termux Assistant.\n",
                YELLOW
            )
        )
