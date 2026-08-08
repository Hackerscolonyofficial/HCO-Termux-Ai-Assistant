# 🔥 HCO TERMUX AI SECURITY ASSISTANT

### 🤖 Termux AI Security Assistant by Azhar HCO Team

> **This code by Azhar HCO Team**

A powerful, colorful, lightweight and beginner-friendly security diagnostics assistant for **Android + Termux**.

HCO Termux AI Security Assistant is designed for learning, security awareness, defensive testing and checking your own Android/Termux environment.

---

# 🚀 About HCO Termux AI Security Assistant

**HCO Termux AI Security Assistant** helps you understand the security condition of your own Android device and Termux environment.

The tool performs local security diagnostics and provides a simple **Security Score** with understandable recommendations.

### 🔐 The tool can check:

- 📱 Android version
- 📱 Device information
- 🧠 RAM
- 💾 Storage
- 🌐 Local IP
- 🌍 DNS configuration
- 🔌 Local listening sockets
- 🔑 SSH / OpenSSH status
- 📦 Termux packages
- 🛡️ Basic privacy posture
- 📊 Security Score
- 📝 Security findings
- 💡 Actionable recommendations
- 📄 JSON security reports

---

# ✨ Features

```text
🔥 HCO ASCII Branding
🎨 Colorful Terminal Interface
🤖 Local Security Assistant
🔐 Security Scanner
📊 Security Score
🌐 Network Diagnostics
🛡️ Privacy Check
🩺 Termux Health Check
🔑 SSH Detection
🌍 DNS Detection
🔌 Local Port / Socket Information
📄 JSON Security Reports
📱 YouTube Support Redirect
```

---

# 📱 TERMUX INSTALLATION

## Step 1 — Install Git

Open Termux and run:

```bash
pkg update -y
```

Then:

```bash
pkg install git -y
```

## Step 2 — Clone The Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

> Replace `YOUR_GITHUB_REPOSITORY_URL` with the GitHub repository URL.

Example:

```bash
git clone https://github.com/YOUR_USERNAME/hco-termux-assistant.git
```

## Step 3 — Enter The Project Directory

```bash
cd hco-termux-assistant
```

## Step 4 — Make Installer Executable

```bash
chmod +x install.sh
```

## Step 5 — Install Requirements

```bash
bash install.sh
```

The installer automatically installs the required packages:

```text
Python
Git
iproute2
net-tools
```

---

# 🚀 RUN THE TOOL

After installation:

```bash
python hco_termux_assistant.py
```

The HCO startup screen will appear.

---

# 📺 YOUTUBE SUPPORT REDIRECT

When the tool starts, it displays the HCO branding and support message.

A countdown will appear:

```text
9
8
7
6
5
4
3
2
1
0
```

After the countdown, the tool attempts to open the **YouTube Android app**.

### ▶️ Hackers Colony Tech

```text
https://youtube.com/@hackers_colony_tech?si=5hYoJ43YgPJ5rzNJ
```

After supporting Hackers Colony, return to Termux and press:

```text
ENTER
```

The main HCO Termux AI Security Assistant will then start.

---

# 🧰 MAIN MENU

The tool contains:

```text
[1] Full Security Scan
[2] Network Diagnostics
[3] Privacy Check
[4] Termux Health
[5] Security Assistant
[6] Open Hackers Colony YouTube
[0] Exit
```

---

# 🔍 1. FULL SECURITY SCAN

Select:

```text
1
```

The scanner checks your local Android/Termux environment.

Example information:

```text
Android
Device
Termux
RAM
Storage
Local IP
DNS
SSH
Packages
Permissions
```

The tool then generates a security score.

Example:

```text
SECURITY SCORE

83/100 • MODERATE
```

---

# 📊 SECURITY SCORE

The score is a simple rule-based indicator.

```text
90 - 100  → GOOD
75 - 89   → MODERATE
50 - 74   → NEEDS ATTENTION
0  - 49   → HIGH ATTENTION
```

The score is **not a complete professional security audit**.

It is intended as a quick educational diagnostic.

---

# ⚠️ ACTIONABLE SECURITY FINDINGS

The tool does not only show a problem.

It also explains what the user can do.

Example:

```text
[MEDIUM] SSH server is installed and appears to be running.

FIX:
If you do NOT use SSH:

pkill sshd

pkg uninstall openssh

If you DO use SSH, keep it and only start it when needed.
```

---

# 🔑 SSH / OPENSSH

Check whether SSH is installed:

```bash
which ssh
```

Check whether SSH server is running:

```bash
pgrep -a sshd
```

If you do not use SSH and want to stop a running SSH server:

```bash
pkill sshd
```

If you never use OpenSSH and want to remove it:

```bash
pkg uninstall openssh
```

### ⚠️ IMPORTANT

If you actually use SSH for legitimate remote access, **do not uninstall OpenSSH**.

Only remove software that you understand and do not need.

---

# 🌐 2. NETWORK DIAGNOSTICS

Select:

```text
2
```

The tool checks information from the current device.

It can display:

```text
Local IP
DNS
Network Interfaces
Local Listening Sockets
```

# 🌍 CHECK LOCAL IP

```bash
ip addr
```

Or:

```bash
ip -brief addr
```

# 🌍 CHECK DNS

```bash
getprop | grep -E 'net\.dns'
```

```bash
cat /etc/resolv.conf
```

If the tool cannot read DNS information but your internet connection works normally, the warning may only be informational.

# 🔌 CHECK LOCAL LISTENING PORTS

```bash
ss -lntup
```

If `ss` is unavailable:

```bash
netstat -lntup
```

Install the required tools:

```bash
pkg install iproute2 net-tools -y
```

### 🛡️ IMPORTANT

This feature checks the **current device only**.

It does not scan random external systems.

---

# 🛡️ 3. PRIVACY CHECK

Select:

```text
3
```

The privacy module displays the security/privacy behavior of the tool.

Example:

```text
Public IP lookup       Not performed
External host scanning Disabled
Password collection   Disabled
Credential extraction Disabled
Local report           Enabled
```

The tool is designed to inspect your own device.

---

# 🩺 4. TERMUX HEALTH

Select:

```text
4
```

The tool checks the Termux environment.

It can check:

```text
Python
Git
curl
ip
ss
Storage
pkg
```

---

# 🤖 5. SECURITY ASSISTANT

Select:

```text
5
```

The local security assistant can explain the latest scan.

Example questions:

```text
security score
```

```text
is my phone secure?
```

```text
check SSH
```

```text
what is DNS?
```

```text
check my network
```

```text
check my phone
```

```text
help
```

Type:

```text
back
```

to return to the main menu.

---

# 📄 SECURITY REPORTS

After a security scan, the tool generates a JSON report.

Reports are saved inside:

```text
~/hco_reports/
```

Example:

```text
security_report_20260808_120000.json
```

The report may contain:

```text
Device
Android
Termux
RAM
Storage
Local IP
DNS
SSH
Network information
Security Score
Findings
Recommendations
Timestamp
```

---

# 🐧 LINUX INSTALLATION

The main tool is designed for **Termux**, but parts of the diagnostics can also be useful on Linux.

## 🐧 Debian / Ubuntu

```bash
sudo apt update
```

```bash
sudo apt install python3 git iproute2 net-tools -y
```

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

```bash
cd hco-termux-assistant
```

```bash
python3 hco_termux_assistant.py
```

## 🐧 ARCH LINUX

```bash
sudo pacman -Syu
```

```bash
sudo pacman -S python git iproute2 net-tools
```

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

```bash
cd hco-termux-assistant
```

```bash
python3 hco_termux_assistant.py
```

# ⚠️ LINUX COMPATIBILITY NOTE

Some Android-specific features may not work on normal Linux.

For example:

```text
getprop
Termux information
Android device properties
```

These commands are Android/Termux specific.

The core diagnostic logic can still be useful on compatible Linux systems.

---

# 🔄 UPDATE THE TOOL

```bash
git pull
```

Then:

```bash
python hco_termux_assistant.py
```

---

# 🗑️ UNINSTALL

```bash
cd ..
```

```bash
rm -rf hco-termux-assistant
```

If you installed OpenSSH and no longer need it:

```bash
pkg uninstall openssh
```

---

# 🛠️ TROUBLESHOOTING

## Python Not Found

```bash
pkg install python -y
```

## Git Not Found

```bash
pkg install git -y
```

## `ss` Command Not Found

```bash
pkg install iproute2 -y
```

## `netstat` Command Not Found

```bash
pkg install net-tools -y
```

## Permission Denied

```bash
chmod +x install.sh
```

Then:

```bash
bash install.sh
```

---

# 📁 PROJECT STRUCTURE

```text
hco-termux-assistant/
│
├── hco_termux_assistant.py
├── install.sh
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🔐 SECURITY & ETHICAL USE

HCO Termux AI Security Assistant is intended for:

```text
✅ Education
✅ Security awareness
✅ Defensive testing
✅ Personal device diagnostics
✅ Termux learning
✅ Linux learning
```

Do NOT use this project for:

```text
❌ Unauthorized access
❌ Credential theft
❌ Phishing
❌ Malware deployment
❌ Attacking external systems
❌ Unauthorized network scanning
❌ Authentication bypass
❌ Exploitation of systems without permission
```

Always obtain permission before testing systems, devices, networks, or accounts that you do not own.

---

# ⚠️ DISCLAIMER

**HCO Termux AI Security Assistant is provided for educational, defensive, and authorized security testing purposes only.**

This software is designed primarily to inspect the user's own Android/Termux environment.

The security score is a **basic rule-based indicator** and should not be considered a professional penetration test, forensic investigation, vulnerability assessment, or guarantee that a device is secure.

The developers and contributors are not responsible for misuse, damage, unauthorized access, data loss, or any illegal activity involving this software.

Use the tool responsibly.

**Learn cybersecurity. Don't abuse it.**

---

# 👨‍💻 DEVELOPER

## 🔥 HACKERS COLONY

### **This code by Azhar HCO Team**

Built with ❤️ by **Hackers Colony** for the cybersecurity, Linux and Termux community.

```text
LEARN
BUILD
TEST
SECURE
SHARE
```

---

# 🌐 CONNECT WITH HACKERS COLONY

## ▶️ YouTube

```text
https://youtube.com/@hackers_colony_tech?si=5hYoJ43YgPJ5rzNJ
```

## 📸 Instagram

```text
https://www.instagram.com/team_hco?igsh=ZTRiMHoydW1rcTJ4
```

## 📘 Facebook

```text
https://www.facebook.com/share/1TemzQjTBF/
```

## 💬 WhatsApp Community

```text
https://chat.whatsapp.com/BGJkixzJMO462C3Az43usC?s=cl&p=a&ilr=0
```

## 📢 Telegram

```text
https://t.me/hackerscolonytech
```

---

# ❤️ DO SUPPORT US

If you find **HCO Termux AI Security Assistant** useful, please support Hackers Colony.

⭐ Star the repository

🍴 Fork the repository

▶️ Subscribe to our YouTube channel

🔔 Turn on the notification bell

📸 Follow us on Instagram

📢 Join our Telegram community

💬 Join our WhatsApp community

📘 Follow us on Facebook

Your support motivates us to build more free cybersecurity, Linux and Termux educational tools.

---

# 📜 LICENSE

This project is released under the:

**MIT License**

See the `LICENSE` file for complete license information.

---

# 🔥 HCO TERMUX AI SECURITY ASSISTANT

```text
╔══════════════════════════════════════════════╗
║                                              ║
║       HCO TERMUX AI SECURITY ASSISTANT       ║
║                                              ║
║          BY AZHAR HCO TEAM                   ║
║                                              ║
╚══════════════════════════════════════════════╝
```

### ❤️ Built for learning.
### 🛡️ Built for security awareness.
### 🔥 Built by Hackers Colony.

**Stay Curious • Stay Ethical • Keep Learning**

---

## ⭐ Thank You For Supporting HCO

**Hackers Colony ❤️**
