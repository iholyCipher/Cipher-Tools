# -*- coding: utf-8 -*-
"""
Cipher Tools - Category 4: Network Reconnaissance & Diagnostics (Tools 31 - 40)
"""
import os
import sys
import time
import socket
import subprocess
import threading

CLR_CYAN = "\033[96m"
CLR_PINK = "\033[95m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_GRAY = "\033[90m"
CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"

def tool_31_arp_sweep():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [31] Local Subnet ARP & Active Host Sweep ==={CLR_RESET}")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        my_ip = s.getsockname()[0]
        s.close()
    except Exception:
        my_ip = "192.168.1.100"
    prefix = ".".join(my_ip.split(".")[:3])
    print(f"  {CLR_CYAN}[*] Sweeping {prefix}.1 - {prefix}.25...{CLR_RESET}")
    active = []
    def ping_worker(ip):
        flag = "-n" if os.name == 'nt' else "-c"
        wait = "-w 350" if os.name == 'nt' else "-W 1"
        if subprocess.call(f"ping {flag} 1 {wait} {ip}", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True) == 0:
            active.append(ip)
    threads = [threading.Thread(target=ping_worker, args=(f"{prefix}.{i}",)) for i in range(1, 26)]
    for t in threads: t.start()
    for t in threads: t.join()
    print(f"  {CLR_GREEN}[✓] Discovered {len(active)} active hosts on local subnet:{CLR_RESET}")
    for a in sorted(active):
        print(f"  ➜ {a}")

def tool_32_port_scanner():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [32] TCP Port Scanner ==={CLR_RESET}")
    target = input("  Enter target IP/Host [default 127.0.0.1]: ").strip() or "127.0.0.1"
    ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 1433, 3000, 3306, 3389, 8000, 8080]
    print(f"  Scanning common ports on {target}...")
    for p in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        if s.connect_ex((target, p)) == 0:
            print(f"  {CLR_GREEN}● Port {p:<5} OPEN{CLR_RESET}")
        s.close()

def tool_33_ping_analyzer():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [33] Ping Latency & Packet Loss Analyzer ==={CLR_RESET}")
    host = input("  Enter target domain or IP (default: 8.8.8.8): ").strip() or "8.8.8.8"
    flag = "-n" if os.name == 'nt' else "-c"
    cmd = ["ping", flag, "4", host]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(res.stdout)

def tool_34_dns_jitter():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [34] DNS Jitter & Multi-Provider Benchmark ==={CLR_RESET}")
    providers = [("Cloudflare", "1.1.1.1"), ("Google", "8.8.8.8"), ("Quad9", "9.9.9.9")]
    for name, s_ip in providers:
        t0 = time.time()
        res = subprocess.run(["ping", "-n", "2", s_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elapsed = (time.time() - t0) / 2 * 1000
        if res.returncode == 0:
            print(f"  {name:<12} ({s_ip}): {CLR_GREEN}{elapsed:.1f} ms{CLR_RESET}")
        else:
            print(f"  {name:<12} ({s_ip}): {CLR_RED}Timeout{CLR_RESET}")

def tool_35_net_adapters():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [35] Network Adapters & MAC Address Matrix ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            cmd = "Get-NetAdapter | Select-Object Name, InterfaceDescription, Status, MacAddress | Format-Table -AutoSize"
            out = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True)
            print(out)
        except Exception as e:
            print(f"  {CLR_RED}[-] Query error: {e}{CLR_RESET}")
    else:
        print("  Windows NetAdapter query.")

def tool_36_active_conns():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [36] Active TCP/UDP Connections Inspector ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            cmd = "netstat -ano | Select-String 'ESTABLISHED' | Select-Object -First 12"
            out = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True)
            print(out)
        except Exception as e:
            print(f"  {CLR_RED}[-] Error: {e}{CLR_RESET}")

def tool_37_gateway_route():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [37] Default Gateway & Routing Table Checker ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            cmd = "Get-NetRoute -DestinationPrefix '0.0.0.0/0' | Select-Object DestinationPrefix, NextHop, InterfaceAlias | Format-Table -AutoSize"
            out = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True)
            print(out)
        except Exception as e:
            print(f"  {CLR_RED}[-] Error: {e}{CLR_RESET}")

def tool_38_reverse_dns():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [38] Hostname to IP & Reverse DNS Lookup ==={CLR_RESET}")
    q = input("  Enter hostname or IP to resolve: ").strip()
    if not q: return
    try:
        if any(c.isalpha() for c in q):
            ip = socket.gethostbyname(q)
            print(f"  {CLR_GREEN}Forward DNS:{CLR_RESET} {q} -> {ip}")
        else:
            host, _, _ = socket.gethostbyaddr(q)
            print(f"  {CLR_GREEN}Reverse DNS:{CLR_RESET} {q} -> {host}")
    except Exception as e:
        print(f"  {CLR_RED}[-] Lookup failed: {e}{CLR_RESET}")

def tool_39_hosts_file():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [39] Local Hosts File Viewer ==={CLR_RESET}")
    hosts_p = r"C:\Windows\System32\drivers\etc\hosts" if os.name == 'nt' else "/etc/hosts"
    if os.path.isfile(hosts_p):
        with open(hosts_p, 'r', encoding='utf-8', errors='ignore') as fp:
            lines = [l.strip() for l in fp if l.strip() and not l.strip().startswith('#')]
        print(f"  Active Non-Commented Mappings ({len(lines)}):")
        for line in lines:
            print(f"  ➜ {line}")
    else:
        print("  Hosts file not accessible.")

def tool_40_wifi_profiles():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [40] Saved WiFi Profiles Inspector ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            out = subprocess.check_output(["netsh", "wlan", "show", "profiles"], text=True)
            for line in out.splitlines():
                if "All User Profile" in line:
                    print(f"  {CLR_GREEN}WiFi:{CLR_RESET} {line.split(':', 1)[1].strip()}")
        except Exception as e:
            print(f"  {CLR_RED}[-] Query error: {e}{CLR_RESET}")
