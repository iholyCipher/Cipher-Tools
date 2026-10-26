<div align="center">

# ⚡ CIPHER TOOLS - TITAN SUITE
### *The Ultimate Cyber, Systems Engineering, Forensics & Network Telemetry Toolkit*

[![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tools](https://img.shields.io/badge/Tools-150%20Built--in%20Modules-success.svg?style=flat-square&color=00ffcc)](https://github.com/ithecipher/Cipher-Tools)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero%20External%20Pip-brightgreen.svg?style=flat-square)](https://github.com/ithecipher/Cipher-Tools)
[![Test Suite](https://img.shields.io/badge/Tests-150%2F150%20Passing%20(100%25)-green.svg?style=flat-square&color=39ff14)](https://github.com/ithecipher/Cipher-Tools)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com/ithecipher/Cipher-Tools)

```text
  ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
 ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
 ██║     ██║██████╔╝███████║█████╗  ██████╔╝       ██║   ██║   ██║██║   ██║██║     ███████╗
 ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗       ██║   ██║   ██║██║   ██║██║     ╚════██║
 ╚██████╗██║██║     ██║  ██║███████╗██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
  ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
```

**Cipher Tools (Titan Suite)** is an enterprise-grade, standalone cybersecurity, binary forensics, hardware benchmarking, and domestic network survival toolkit. Packed with **150 precision tools** across **11 core engineering categories**, it runs natively on standard Python with **zero external pip dependencies**.

[English](#-key-features) • [فارسی](#-معرفی-فارسی-راهنمای-کامل) • [Quick Start](#-quick-start) • [CLI Flags](#-cli-flags--headless-execution) • [Tools Directory](#-complete-150-tool-catalog) • [Testing](#-automated-testing)

---

</div>

## 🌟 Key Features

- **🔋 150 Native Built-in Tools:** Every single tool is fully implemented in Python—no external script launchers or wrappers.
- **⚡ Zero Mandatory Dependencies:** Runs out of the box on Python 3.8+ using pure standard library modules (`os`, `sys`, `socket`, `hashlib`, `ssl`, `ctypes`, etc.).
- **🖥️ Dual Mode (Interactive REPL + Headless CLI):** Use the cyberpunk interactive terminal or execute tools directly from scripts, CI/CD pipelines, or terminal one-liners.
- **🌐 50 Specialized Domestic & Censorship Diagnostics:** In-depth network analysis, DNS poisoning detection, Cloudflare clean IP sweeps, DPI reset detection, and multi-protocol VPN testing.
- **🛡️ Enterprise Forensics & Security:** Hex dumps, PE binary header analysis, Shannon file entropy, DoD 5220.22-M 3-pass file shredder, ADS stream detector.
- **🧪 100% Automated Test Coverage:** Built-in self-test engine (`test_suite.py`) validating every tool under 30 seconds.

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/ithecipher/Cipher-Tools.git
cd Cipher-Tools
```

### 2. Launch Interactive Suite
```bash
python cipher_tools.py
```

### 3. Optional: Install as Global System CLI
```bash
pip install -e .
cipher-tools --help
```

---

## ⚡ CLI Flags & Headless Execution

Cipher Tools can be completely automated without launching the interactive menu:

| Flag | Description | Example |
| :--- | :--- | :--- |
| `-t, --tool <ID>` | Direct launch of any tool by ID (1–150) | `python cipher_tools.py --tool 41` |
| `-s, --search <query>` | Instant keyword search across all 150 tools | `python cipher_tools.py --search dns` |
| `-c, --category <C#>` | Browse category by index (1–11) | `python cipher_tools.py --category 11` |
| `-l, --list` | Print the full categorized catalogue | `python cipher_tools.py --list` |
| `--json` | Export the entire 150-tool directory as JSON | `python cipher_tools.py --json` |
| `--test` | Run automated self-diagnostic integrity check | `python cipher_tools.py --test` |
| `--info <ID>` | View metadata and description of a tool | `python cipher_tools.py --info 101` |
| `-v, --version` | Output version string | `python cipher_tools.py --version` |

---

## 📚 Complete 150-Tool Catalog

<details open>
<summary><b>📂 Category 1: System, OS & Kernel (Tools 1 - 10)</b></summary>

| ID | Tool Name | Description |
|:---:|:---|:---|
| **01** | `OS Architecture & Kernel Build Info` | Windows build specs, architecture, machine specifications & Python runtime |
| **02** | `Windows Uptime & Boot Time Tracker` | Computes accurate system uptime and boot timestamp via CIM |
| **03** | `Installed Hotfixes & OS Updates` | Lists installed Windows hotfixes, patches and updates |
| **04** | `Environment Variables Explorer` | Inspects all active system and user environment variables |
| **05** | `System PATH Validator & Missing Path Detector` | Detects valid and broken/missing directories in system PATH |
| **06** | `Windows Power Scheme & Battery Status` | Power plan, active AC line, and battery charge percentage |
| **07** | `Active Logged-in Sessions & Users` | Inspects user sessions, operator identities, and domain configurations |
| **08** | `BIOS / Motherboard Serial & Manufacturer` | Motherboard model, manufacturer, and BIOS serial identifiers |
| **09** | `System Locale, Codepage & Timezone` | System encoding, UTC/local clock, codepage and timezone telemetry |
| **10** | `Windows Shutdown / Reboot Timer` | Schedules or aborts delayed shutdown and restart operations |

</details>

<details>
<summary><b>⚡ Category 2: CPU, Memory & Hardware Benchmarks (Tools 11 - 20)</b></summary>

| ID | Tool Name | Description |
|:---:|:---|:---|
| **11** | `Multi-Threaded Floating-Point Benchmark (FLOPs)` | Parallel trigonometric FLOPs calculation across all logical cores |
| **12** | `Single-Thread Integer Math Stress Test` | Arithmetic bitwise and modulus operations measuring MOps/sec |
| **13** | `RAM Memory Architecture & Capacity` | Total physical RAM, available memory, and architecture report |
| **14** | `Real-time CPU Usage Meter (Polled)` | Real-time processor load percentage sampling |
| **15** | `Process Affinity & CPU Core Count Matrix` | Enumerates CPU core threads and logical nodes |
| **16** | `Memory Bandwidth Throughput Test` | Measures direct RAM read/write throughput speed in MB/s |
| **17** | `Top 15 Memory-Consuming Processes` | Identifies and sorts processes using the most RAM |
| **18** | `Process Killer by PID or Process Name` | Terminates unruly processes forcefully |
| **19** | `Process Hierarchy & Parent ID` | Maps parent process IDs (PPID) to child processes |
| **20** | `Real-time System Heartbeat Pulse` | Live pulse monitoring system responsiveness and scheduling |

</details>

<details>
<summary><b>💾 Category 3: Storage, Disk & File System Forensics (Tools 21 - 30)</b></summary>

| ID | Tool Name | Description |
|:---:|:---|:---|
| **21** | `Partition Capacity & Percentage Bar Graph` | Visual ASCII bar graph of storage across all system drives |
| **22** | `SHA-256 Duplicate File Finder` | Cryptographic deduplication detector identifying identical files |
| **23** | `Recursive Directory Space Consumption Tree` | Sorted disk usage explorer for folders and files |
| **24** | `Ghost Folder Pruner (Empty Directory Eraser)` | Recursively removes empty orphaned directories |
| **25** | `Smart Archive Search, Auto-Extract & Launch` | Searches ZIP/RAR/7z archives, auto-extracts and opens Explorer |
| **26** | `Batch File Extension Renamer` | Mass extension rename tool across directory trees |
| **27** | `Checksum Manifest Creator (.sha256)` | Generates SHA-256 digital integrity manifests for folders |
| **28** | `Checksum Manifest Verifier` | Audits folder contents against cryptographic manifests |
| **29** | `Zero-Byte / Corrupted File Finder` | Scans for damaged, empty zero-byte files |
| **30** | `Largest Files Finder in Target Directory` | Ranks the largest files in any specified folder |

</details>

<details>
<summary><b>📡 Category 4: Network Reconnaissance & Diagnostics (Tools 31 - 40)</b></summary>

| ID | Tool Name | Description |
|:---:|:---|:---|
| **31** | `Local Subnet ARP & Active Host Sweep` | Sweeps local subnet and reveals active live IP hosts |
| **32** | `TCP Port Scanner (Common Services)` | Scans critical TCP ports (SSH, HTTP, HTTPS, DB, RDP) |
| **33** | `Ping Latency & Packet Loss Analyzer` | High-precision ICMP latency and loss probe |
| **34** | `DNS Jitter & Multi-Provider Benchmark` | Benchmarks Cloudflare, Google, and Quad9 response times |
| **35** | `Network Interface Adapters & MAC Address Matrix` | Enlists active NICs, MAC addresses, and interface statuses |
| **36** | `Active TCP/UDP Connections Inspector (Netstat)` | Identifies active socket connections and listening ports |
| **37** | `Default Gateway & Routing Table Checker` | Default routes and network gateway validation |
| **38** | `Hostname to IP / Reverse DNS Lookup` | Forward IP resolution and Reverse DNS lookups |
| **39** | `Local Hostname Resolution & Hosts File Viewer` | Inspects active system hosts file records |
| **40** | `WiFi Profile & Signal Inspector (netsh wlan)` | Lists saved Wi-Fi profiles and SSIDs |

</details>

<details>
<summary><b>🌐 Category 5: Web & Internet Intelligence (Tools 41 - 50)</b></summary>

| ID | Tool Name | Description |
|:---:|:---|:---|
| **41** | `Public IP, Geolocation & ISP Telemetry` | Retrieves public IP, country, city, and ISP organisation |
| **42** | `HTTP/HTTPS Header & Server Banner Grabber` | Inspects HTTP response headers and web server banners |
| **43** | `Website SSL/TLS Certificate Expiration Checker` | Verifies SSL cert validity, issuer, and expiration date |
| **44** | `Website Response Time & Status Code Prober` | Measures HTTP status code and millisecond latency |
| **45** | `Fast URL Downloader (CLI Wget style)` | Direct file download utility |
| **46** | `Robots.txt & Sitemap Fetcher` | Fetches and displays crawler indexing rules |
| **47** | `URL Expander (Follow Redirect Chains)` | Unmasks shortened URLs and traces redirection hops |
| **48** | `HTML Title & Meta Tags Extractor` | Scrapes web titles and meta information |
| **49** | `Domain Whois & Registrar Probe` | Resolves authoritative DNS addresses and records |
| **50** | `Internet Connectivity Continuous Monitor` | Multi-probe socket connectivity tester |

</details>

<details>
<summary><b>🔐 Category 6: Cryptography, Hashes & Ciphers (Tools 51 - 60)</b></summary>

| ID | Tool Name | Description |
|:---:|:---|:---|
| **51** | `Multi-Hash Calculator (MD5, SHA1, SHA256, SHA512)` | Simultaneous multi-algorithm cryptographic hashing |
| **52** | `Hash Type Algorithmic Identifier` | Identifies unknown hash signatures by length and format |
| **53** | `Symmetric XOR Stream Cipher` | Encrypts and decrypts text streams using bitwise XOR |
| **54** | `Base16 (Hex), Base32 & Base64 Encoder/Decoder` | Multi-radix data encoding and decoding utility |
| **55** | `Caesar / ROT13 Substitution Cipher` | Classical rotation cipher transformations |
| **56** | `High-Entropy Password & Token Matrix` | Cryptographically secure random tokens and passwords |
| **57** | `Shannon Entropy Password Strength Grader` | Computes information entropy bits for password security |
| **58** | `HMAC SHA-256 Signature Generator` | Generates keyed-hash message authentication codes |
| **59** | `Secure Random Number / Dice Generator` | High-entropy random integers, bytes, and dice rolls |
| **60** | `UUID / GUID Generator (v4 Cryptographic)` | Generates RFC 4122 random UUIDs |

</details>

<details>
<summary><b>🛡️ Category 7: Cybersecurity, Defense & Sanitization (Tools 61 - 70)</b></summary>

| ID | Tool Name | Description |
|:---:|:---|:---|
| **61** | `DoD 5220.22-M 3-Pass Military File Shredder` | Overwrites files with 0x00, 0xFF, and random bytes before unlinking |
| **62** | `Free Space Zero-Fill Wiper (Anti-Forensics)` | Flushes unallocated sectors to prevent file recovery |
| **63** | `Windows Clipboard Security Sanitizer` | Clears and nullifies clipboard contents from memory |
| **64** | `Windows Temp & Crash Dump Purger` | Sanitizes residual crash dumps and temporary cache files |
| **65** | `Browser Cache Cleaner Helper` | Inspects and audits local browser cache storage |
| **66** | `Suspicious Binaries in AppData Inspector` | Scans AppData for rogue `.exe`, `.dll`, or `.vbs` files |
| **67** | `USB Drive Autorun & Shortcut Virus Scanner` | Scans removable media for malicious `autorun.inf` |
| **68** | `NTFS Alternate Data Stream (ADS) Detector` | Uncovers hidden data streams attached to NTFS files |
| **69** | `Windows Firewall Status & Profile Inspector` | Audits state of Domain, Private, and Public firewall profiles |
| **70** | `User Account Control (UAC) Elevation Level Checker` | Asserts process security token and administrator rights |

</details>

<details>
<summary><b>🔬 Category 8: Binary Forensics & Reverse Engineering (Tools 71 - 80)</b></summary>

| ID | Tool Name | Description |
|:---:|:---|:---|
| **71** | `Binary Hex Viewer (Hex Dump with ASCII column)` | Formatted hexadecimal viewer with printable ASCII panel |
| **72** | `Magic Bytes / File Header Signature Identifier` | Determines real file formats by header signatures (MZ, ELF, PNG, etc.) |
| **73** | `ASCII & Unicode String Extractor` | Extracts embedded human-readable strings from binaries |
| **74** | `PE Executable Header & Section Analyzer` | Inspects Windows PE DOS stubs, COFF headers, and offsets |
| **75** | `File Entropy Calculator (Packed / Encrypted Binary)` | Detects packers, cryptors, and compression via Shannon entropy |
| **76** | `Binary Difference Comparator` | Byte-by-byte visual diff comparator between two files |
| **77** | `Base64 Extractor from Binary Data` | Hunts for Base64 encoded blobs inside raw binaries |
| **78** | `IP / URL Regex Finder in Binary Files` | Scrapes IP addresses and URLs from compiled files |
| **79** | `File Timestamp Forgery / Timestomp Detector` | Inspects creation, modification, and access time anomalies |
| **80** | `File MIME Type Guessing Engine` | Resolves content types using system mime databases |

</details>

<details>
<summary><b>🪟 Category 9: Windows Administration & Registry (Tools 81 - 90)</b></summary>

| ID | Tool Name | Description |
|:---:|:---|:---|
| **81** | `Windows Startup Items & Registry Run Keys` | Audits startup applications and persistence keys |
| **82** | `Windows Services Inspector & Status Query` | Lists active running services and display names |
| **83** | `Windows Event Viewer Critical Errors Log` | Fetches recent critical errors from the System Event Log |
| **84** | `Installed Software & Programs Inventory` | Queries registry for installed software packages |
| **85** | `Windows Defender Anti-Malware Engine Status` | Checks Real-time Protection, Antivirus state, and signature age |
| **86** | `DNS Cache Flush Utility (ipconfig /flushdns)` | Purges local DNS resolver cache |
| **87** | `Task Scheduler Active Jobs Query` | Enumerates active scheduled jobs and triggers |
| **88** | `Windows Product Key / Digital License Query` | Queries licensing status via SoftwareLicensingProduct |
| **89** | `System File Integrity Checker (SFC helper)` | Quick reference and launcher for SFC and DISM repair |
| **90** | `Windows Update Service State Inspector` | Checks `wuauserv` service health and startup type |

</details>

<details>
<summary><b>🛠️ Category 10: Productivity, Converters & Developer Utilities (Tools 91 - 100)</b></summary>

| ID | Tool Name | Description |
|:---:|:---|:---|
| **91** | `Unix Epoch Timestamp Converter` | Converts between UNIX timestamps and human-readable dates |
| **92** | `JSON Pretty Printer & Syntax Validator` | Validates, indents, and reformats JSON payloads |
| **93** | `XML / HTML Tag Stripper` | Strips tags and extracts clean textual content |
| **94** | `IP Subnet Mask & CIDR Calculator` | Computes subnet masks and usable host counts from prefix |
| **95** | `Number Base Converter (Bin, Oct, Dec, Hex)` | Interconverts numbers across decimal, hexadecimal, binary & octal |
| **96** | `Text Word, Line & Character Counter` | Analyzes words, characters, and estimated reading time |
| **97** | `Text Case Converter (camel, snake, kebab, Pascal)` | Converts text strings across programming case conventions |
| **98** | `Markdown to Plain Text Stripper` | Strips markdown formatting into clean raw text |
| **99** | `Regex Pattern Matcher & Tester` | Tests regular expressions in real-time with sample input |
| **100** | `Developer Scratchpad & Quick Note Vault` | Local lightweight scratchpad for developer notes |

</details>

<details>
<summary><b>📡 Category 11: National Network & Domestic Telemetry (Tools 101 - 150)</b></summary>

| ID | Tool Name | Description |
|:---:|:---|:---|
| **101** | `Net Melli vs International Internet Detector` | Concurrent probe determining if global internet is disconnected |
| **102** | `Massive DNS Benchmark (26 DNS Providers)` | Benchmarks Shecan, 403, Electro, Radar, Begzar & global DNS |
| **103** | `DNS Poisoning & Spoofing Hunter` | Detects hijacked resolutions and fake `10.10.34.34` responses |
| **104** | `Massive VPN & Proxy Core Port Scanner (45+ Ports)` | Scans essential proxy/VPN ports (SSH, VMess, VLESS, Hysteria, WireGuard) |
| **105** | `Domestic IP & Nim-Baha Traffic Inspector` | Checks whether target addresses are routed via domestic intranet |
| **106** | `Domestic CDN Download Speed Test` | Tests raw download throughput from domestic CDN mirrors |
| **107** | `Banking & Essential Portals Status` | Monitors accessibility of Shaparak, Shetab and banking gateways |
| **108** | `Tehran IXP & Domestic Gaming Latency Probe` | Measures latency to domestic peering exchange points |
| **109** | `Windows Hosts DNS Bypass Injector` | Injects clean IP-to-domain mappings into Windows hosts |
| **110** | `Net Melli Emergency Cheat-Sheet & Mirrors` | Complete survival runbook for domestic packages (PyPI, Ubuntu, Docker) |
| **111** | `Cloudflare Clean Subnet Scanner` | Scans Cloudflare CIDR blocks for low-latency clean IPs |
| **112** | `TLS Handshake & Packet Drop Inspector` | Measures TLS negotiation timing and packet drops |
| **113** | `DPI Fake TCP RST Packet Detector` | Detects deep packet inspection injection of reset flags |
| **114** | `Optimal MTU Discovery Tool` | Computes optimal MTU to eliminate packet fragmentation |
| **115** | `DNS-over-HTTPS (DoH) vs Plain UDP DNS Benchmark` | Compares secure DoH response times against plain UDP |
| **116** | `Local SOCKS5 Proxy Latency Benchmark` | Evaluates local proxy latency (`127.0.0.1:10808` / `7890`) |
| **117** | `Local HTTP Tunnel Proxy Speed Test` | Measures throughput over local HTTP proxy tunnels |
| **118** | `Network Operator & ASN Detector` | Identifies ISP, autonomous system number, and IP owner |
| **119** | `Routing Table & Split-Tunneling Inspector` | Validates split routing rules across network interfaces |
| **120** | `Automated Shecan / 403 DNS Configurator` | One-click configuration of anti-sanction DNS on active NIC |
| **121** | `Reset DNS to DHCP Default` | Restores network adapter DNS back to automatic DHCP |
| **122** | `Enable Windows System Proxy` | Programmatically activates Windows system proxy settings |
| **123** | `Disable Windows System Proxy` | Disables system proxy and clears routing overrides |
| **124** | `Academic & University Portals Health Check` | Verifies reachability of educational and testing portals |
| **125** | `Domestic Banking Deep Latency Check` | High-precision latency analysis across major banking switches |
| **126** | `Domestic Messengers Reachability Probe` | Tests connectivity to Bale, Eitaa, Rubika, and Soroush |
| **127** | `Global Messengers Filtering Auditor` | Assesses filtering status of Telegram, WhatsApp, and X |
| **128** | `Domestic VOD & Streaming Speed Check` | Tests performance of national streaming services |
| **129** | `Domestic Packet Loss & Jitter Stress Test` | 20-packet stress probe measuring packet drop rates |
| **130** | `Domestic Git & Open Source Repository Mirrors` | Reference list of national mirrors for developer tools |
| **131** | `SNI & DPI Filtering Inspector` | Probes SNI blocking mechanisms on remote endpoints |
| **132** | `WebSocket & gRPC Port Prober` | Tests reachability of WebSocket and gRPC proxy endpoints |
| **133** | `UDP Choking & Throttling Test` | Detects UDP protocol throttling and packet drops |
| **134** | `Hysteria & TUIC Protocol Prober` | Probes modern QUIC/UDP-based proxy protocols |
| **135** | `WireGuard Handshake Simulator` | Simulates UDP initiation packets for WireGuard tunnels |
| **136** | `National NTP Time Synchronization` | Audits time drift against domestic NTP servers |
| **137** | `Traceroute to Border Gateways` | Visualizes route hops to national border gateway nodes |
| **138** | `National IP Half-Price Database Query` | Checks IP addresses against national regulatory lists |
| **139** | `DNS & Gateway Leak Detector` | Verifies whether DNS queries leak outside proxy tunnels |
| **140** | `Network Adapter Reset & DNS Purger` | Complete network stack flush and adapter reset |
| **141** | `PyPI Domestic Mirror Auto-Configurator` | One-click setup for high-speed national PyPI mirrors |
| **142** | `NPM Domestic Registry Auto-Configurator` | Replaces npm registry with domestic mirrors |
| **143** | `Docker Hub Domestic Mirrors & Bypass Guide` | Comprehensive guide and config for Docker registry mirrors |
| **144** | `Tehran IXP Peering & BGP Routing Summary` | Summary of internal BGP peering and traffic exchanges |
| **145** | `v2ray VMess / VLESS Config Link Decoder` | Decodes `vmess://` and `vless://` strings into readable JSON |
| **146** | `Subscription Link Fetcher & Base64 Extractor` | Downloads and decodes proxy configurations from sub links |
| **147** | `Cloudflare Clean IP Ping & Latency Matrix` | Evaluates clean Cloudflare IP candidates for proxies |
| **148** | `Iranian App Stores Connection Tester` | Tests accessibility of Cafe Bazaar, Myket, and Sibapp |
| **149** | `Windows TCP Auto-Tuning Optimization` | Optimizes TCP congestion window to combat packet loss |
| **150** | `Master Dashboard & Survival Guide Net Melli` | Emergency survival summary and master crisis runbook |

</details>

---

## 🧪 Automated Testing

Cipher Tools includes a complete automated test runner. Run all 150 tool tests with a single command:

```bash
python test_suite.py
```

Or directly via the CLI:
```bash
python cipher_tools.py --test
```

Output:
```text
====================================================================
🚀 CIPHER TOOLS - EXHAUSTIVE 150-TOOL QUALITY ASSURANCE SUITE
====================================================================
  [✓] Tool 001 PASSED | System     | OS Architecture & Kernel Build Info
  [✓] Tool 002 PASSED | System     | Windows Uptime & Boot Time Tracker
  ...
  [✓] Tool 150 PASSED | NatNet     | Master Dashboard & Survival Guide
====================================================================
TEST RESULTS SUMMARY:
  Total Tools Tested : 150
  Passed             : 150 (100.0%)
  Failed             : 0
  Total Time         : 25.40 seconds
====================================================================
🌟 ALL 150 TOOLS PASSED WITH 100% SUCCESS RATE! 🌟
```

---

## 🇮🇷 معرفی فارسی (راهنمای کامل)

**Cipher Tools - Titan Suite** کامل‌ترین سوئیت ابزارهای تخصصی سیستم، شبکه، فارنزیک باینری، تست سخت‌افزار و خط فرمان برای سیستم‌عامل ویندوز و لینوکس است. این پروژه دارای **۱۵۰ ابزار مستقل و کدنویسی‌شده به زبان پایتون** است که بدون نیاز به نصب حتی یک کتابخانه جانبی (`pip`) و کاملاً مستقل اجرا می‌شود.

### 🌟 ویژگی‌های برجسته:
۱. **۱۵۰ ابزار کاملاً بومی و آماده به کار:** هیچ ابزاری وابسته به اسکریپت‌های دانلودی خارجی نیست.
۲. **۵۰ ابزار اختصاصی شرایط نت ملی و دور زدن اختلالات:** تست پینگ DNSهای تحریم‌شکن (شکن، ۴۰۳، الکترو، رادار)، اسکنر ۴۵ پورت حیاتی وی‌پی‌ان، سنجش آی‌پی‌های کلین کلودفلر، دیکودر لینک‌های v2ray، و بهینه‌سازی TCP ویندوز.
۳. **سوئیت تست خودکار ۱۰۰٪:** تمام ۱۵۰ ابزار دارای سیستم تست خودکار با خروجی ۱۰۰٪ موفقیت هستند.
۴. **پشتیبانی کامل از خط فرمان (Headless / CLI):** امکان اجرای تکی هر ابزار (مانند `python cipher_tools.py --tool 101`) یا خروجی ساختاریافته JSON برای برنامه‌های دیگر.

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <b>Built for Engineers, Defenders & Explorers worldwide.</b><br>
  <sub>Contributions, issues, and feature requests are welcome!</sub>
</div>
