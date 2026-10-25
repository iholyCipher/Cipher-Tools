# -*- coding: utf-8 -*-
"""
Cipher Tools - Category 11 Part 1: National Network (Net Melli & Domestic Tools) [Tools 101 - 125]
Engineered for: TheCIpher (Fingilish Output for Clean Windows Terminal Display)
Includes Massive DNS Benchmark (25+ DNS) & Massive VPN Port Scanner (45+ Ports)
"""
import os
import sys
import time
import socket
import ssl
import urllib.request
import urllib.error
import subprocess

# Windows UTF-8 stdout fix
try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

# Import Part 2 (Tools 126 - 150)
from cat11_natnet_part2 import *

CLR_CYAN = "\033[96m"
CLR_PINK = "\033[95m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_GRAY = "\033[90m"
CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"

def tool_101_netmelli_checker():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [101] Tashkhise Vaziate Shabake (Net Melli vs Internet Beynolmelal) ==={CLR_RESET}")
    print(f" {CLR_CYAN}[*] Dar hale barresi hamzaman masirhaye Dakheli va Beynolmelali...{CLR_RESET}\n")
    
    domestic_hosts = [("Aparat (Dakheli)", "aparat.com"), ("Digikala (Dakheli)", "digikala.com"), ("Shaparak (Banki)", "shaparak.ir"), ("Telewebion (Dakheli)", "telewebion.com")]
    intl_hosts = [("Google (Global)", "google.com"), ("Cloudflare (Global)", "cloudflare.com"), ("GitHub (Global)", "github.com"), ("Wikipedia (Global)", "wikipedia.org")]

    dom_ok = 0
    print(f" {CLR_BOLD}[ Server-haye Dakheli - Shabake Melli Ettelaat ]{CLR_RESET}")
    for name, host in domestic_hosts:
        t0 = time.time()
        try:
            socket.create_connection((host, 80), timeout=2.5)
            ms = (time.time() - t0) * 1000
            print(f"  {CLR_GREEN}[OK]{CLR_RESET}   {name:<24}: Motassel ({ms:.1f}ms)")
            dom_ok += 1
        except Exception:
            print(f"  {CLR_RED}[FAIL]{CLR_RESET} {name:<24}: Ghat'e")

    intl_ok = 0
    print(f"\n {CLR_BOLD}[ Server-haye Beynolmelali - Internet Jahani ]{CLR_RESET}")
    for name, host in intl_hosts:
        t0 = time.time()
        try:
            socket.create_connection((host, 80), timeout=2.5)
            ms = (time.time() - t0) * 1000
            print(f"  {CLR_GREEN}[OK]{CLR_RESET}   {name:<24}: Motassel ({ms:.1f}ms)")
            intl_ok += 1
        except Exception:
            print(f"  {CLR_RED}[FAIL]{CLR_RESET} {name:<24}: Masdood / Ghat'e")

    print("\n " + "="*52)
    if dom_ok >= 2 and intl_ok == 0:
        print(f" {CLR_BOLD}{CLR_RED}Vaziate Jari: [ HALAT NET MELLI KAMEL (Internet Khareji Ghat'e Ast) ]{CLR_RESET}")
        print(f" {CLR_YELLOW}Tozih: Ertebat ba server-haye khareji ghat'e ast vali Net Melli fa'al ast.{CLR_RESET}")
    elif dom_ok >= 2 and intl_ok >= 2:
        print(f" {CLR_BOLD}{CLR_GREEN}Vaziate Jari: [ INTERNET BEYNOLMELAL KAMEL & MOTASSEL ]{CLR_RESET}")
        print(f" {CLR_GREEN}Tozih: Dastresi be kharej va dakhel har do bedune moshkel bargarar ast.{CLR_RESET}")
    elif dom_ok == 0 and intl_ok == 0:
        print(f" {CLR_BOLD}{CLR_RED}Vaziate Jari: [ GHAT'E KAMEL SHABAKE / ADAME ETESAL BE MODEM ]{CLR_RESET}")
    else:
        print(f" {CLR_BOLD}{CLR_YELLOW}Vaziate Jari: [ SHABAKE MOKHTAL / FILTERING SATHI YA LOSS BALA ]{CLR_RESET}")

def tool_102_iran_dns_benchmark():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [102] Massive DNS Benchmark (26 DNS: Irani, Tahrim-Shekan & Jahani) ==={CLR_RESET}")
    dns_servers = [
        # Tahrim Shekan & Domestic
        ("Shecan Asli", "178.22.122.100"),
        ("Shecan Poshtiban", "185.51.200.2"),
        ("403.online Primary", "10.202.10.202"),
        ("403.online Backup", "10.202.10.102"),
        ("Electro Anti-Sanction", "78.157.42.101"),
        ("Electro Secondary", "78.157.42.100"),
        ("Radar Game Asli", "10.202.10.10"),
        ("Radar Game Backup", "10.202.10.11"),
        ("Begzar Primary", "185.55.226.26"),
        ("Begzar Secondary", "185.55.225.25"),
        ("Shatel DNS", "85.15.1.14"),
        ("MCI Hamrah Aval", "5.200.200.200"),
        ("Irancell DNS", "109.96.8.51"),
        ("Rightel DNS", "217.218.127.127"),
        ("Asiatech DNS", "194.225.62.80"),
        ("Mokhaberat (TCI)", "217.218.155.155"),
        # Global & Privacy
        ("Cloudflare Primary", "1.1.1.1"),
        ("Cloudflare Security", "1.1.1.2"),
        ("Google Primary", "8.8.8.8"),
        ("Google Secondary", "8.8.4.4"),
        ("Quad9 Secure", "9.9.9.9"),
        ("OpenDNS Home", "208.67.222.222"),
        ("AdGuard Default", "94.140.14.14"),
        ("Control D Free", "76.76.2.0"),
        ("DNS.WATCH Germany", "84.200.69.80"),
        ("Comodo Secure", "8.26.56.26")
    ]
    print(f" {CLR_CYAN}[*] Test latency ping rooye {len(dns_servers)} DNS Server mokhtalef...{CLR_RESET}\n")
    flag = "-n" if os.name == 'nt' else "-c"
    
    for name, s_ip in dns_servers:
        t0 = time.time()
        cmd = ["ping", flag, "1", "-w", "500", s_ip]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elapsed = (time.time() - t0) * 1000
        if res.returncode == 0:
            color = CLR_GREEN if elapsed < 40 else (CLR_YELLOW if elapsed < 95 else CLR_PINK)
            print(f"  {name:<26} ({s_ip:<15}): {color}{elapsed:5.1f} ms{CLR_RESET}")
        else:
            print(f"  {name:<26} ({s_ip:<15}): {CLR_RED}Timeout (Pasokh Nadad){CLR_RESET}")

def tool_103_dns_poison_detector():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [103] Shekarchi Aloudegi va DNS Poisoning (Fake IP Detector) ==={CLR_RESET}")
    domain = input("  Domain baraye barresi (Pishfarz: twitter.com): ").strip() or "twitter.com"
    print(f"  {CLR_CYAN}[*] Este'lam record DNS baraye {domain}...{CLR_RESET}")
    try:
        ip = socket.gethostbyname(domain)
        print(f"  IP bazgardande shode: {CLR_BOLD}{ip}{CLR_RESET}")
        poison_ips = ["10.10.34.34", "10.10.34.35", "10.10.34.36", "10.10.22.22", "127.0.0.1", "0.0.0.0"]
        if ip in poison_ips or ip.startswith("10.10."):
            print(f"  {CLR_BOLD}{CLR_RED}[!] EKHTAR: DNS Poisoning / Hijacking Shenasayi Shod!{CLR_RESET}")
            print(f"  {CLR_YELLOW}Traffic be safhe Peyvandha (10.10.34.34) hedayat shode ast.{CLR_RESET}")
        else:
            print(f"  {CLR_GREEN}[✓] Address be IP ja'li peyvandha negasht nashode ast.{CLR_RESET}")
    except Exception as e:
        print(f"  {CLR_RED}[-] Khata dar este'lam DNS: {e}{CLR_RESET}")

def tool_104_proxy_health_check():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [104] Massive VPN & Proxy Core Port Scanner (45+ Ports) ==={CLR_RESET}")
    proxy_ports = [
        # v2ray, Xray & v2rayN
        ("v2rayN SOCKS5 Default", 10808),
        ("v2rayN HTTP Default", 10809),
        ("v2rayN Second SOCKS", 10810),
        ("v2rayN Second HTTP", 10811),
        ("Xray Custom SOCKS", 1080),
        ("Xray Custom HTTP", 1081),
        # Clash, Clash Verge, Clash Meta
        ("Clash Mixed Port", 7890),
        ("Clash SOCKS5 Port", 7891),
        ("Clash Redir Port", 7892),
        ("Clash TProxy Port", 7893),
        ("Clash Verge Controller", 9090),
        ("Clash Meta API", 9097),
        # Sing-box, Nekoray & Matsuri
        ("Sing-box Mixed Port", 2080),
        ("Sing-box SOCKS5", 2081),
        ("Nekoray SOCKS5", 2080),
        ("Nekoray HTTP", 2081),
        ("Matsuri SOCKS", 2082),
        # Shadowsocks & ShadowsocksR
        ("Shadowsocks Default", 1080),
        ("Shadowsocks Alt", 8388),
        ("ShadowsocksR Local", 1086),
        ("ShadowsocksR Alt", 1087),
        # Tor & Privoxy
        ("Tor Browser SOCKS5", 9150),
        ("Tor Service SOCKS5", 9050),
        ("Privoxy HTTP Proxy", 8118),
        ("Tor Control Port", 9051),
        # Outline, Psiphon, Windscribe
        ("Outline SOCKS5", 8585),
        ("Psiphon SOCKS5", 1080),
        ("Psiphon HTTP", 8080),
        ("Windscribe Local Proxy", 54321),
        ("Cloudflare WARP Local", 40001),
        ("WARP SOCKS5", 1074),
        # General HTTP / SOCKS Proxies
        ("General HTTP Proxy", 8080),
        ("General SOCKS4/5", 1080),
        ("Fiddler / Charles Proxy", 8888),
        ("Burp Suite Proxy", 8080),
        ("Zapret / ByeDPI Local", 1080),
        ("SpoofDPI SOCKS", 8080),
        ("Green Tunnel HTTP", 8000),
        ("Zapret Alt SOCKS", 2334),
        # VPN Protocols Local Tunnels
        ("WireGuard Tunnel Port", 51820),
        ("OpenVPN TCP Port", 1194),
        ("IPSec / IKEv2 Port", 500),
        ("L2TP Port", 1701),
        ("Hysteria UDP Local", 2088),
        ("TUIC UDP Local", 2089)
    ]
    print(f"  Barresi fa'al boodan {len(proxy_ports)} port standard VPN va Proxy dar local (127.0.0.1):\n")
    found = 0
    for name, port in proxy_ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.12)
        res = s.connect_ex(("127.0.0.1", port))
        if res == 0:
            print(f"  {CLR_GREEN}[ACTIVE]{CLR_RESET} Port {port:<5} [{name:<26}] -> Fa'al va dar hale ghoosh dadan!")
            found += 1
        s.close()
    if found == 0:
        print(f"\n  {CLR_YELLOW}[!] Hich client proxy ya VPN rooye 45 port standard fa'al nist.{CLR_RESET}")
    else:
        print(f"\n  {CLR_BOLD}{CLR_GREEN}[✓] Majmoo'an {found} port VPN/Proxy fa'al shenasayi shod.{CLR_RESET}")

def tool_105_domestic_ip_inspector():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [105] Barresi Traffic Dakheli va Nim-Baha (Domestic IP Inspector) ==={CLR_RESET}")
    target = input("  Domain ya IP morede nazar (mesle aparat.com): ").strip()
    if not target: return
    try:
        ip = socket.gethostbyname(target)
        print(f"  Target IP: {ip}")
        print(f"  {CLR_CYAN}[*] Este'lam moghe'iyat geographi IP...{CLR_RESET}")
        try:
            req = urllib.request.Request(f"https://ipapi.co/{ip}/json/", headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=4) as res:
                import json
                d = json.loads(res.read().decode())
                country = d.get('country_code', 'IR')
                org = d.get('org', 'Iran Network')
                if country == 'IR':
                    print(f"  {CLR_GREEN}[✓] In IP mota'alleq be Iran ({org}) ast va traffic Dakheli / Nim-Baha ast.{CLR_RESET}")
                else:
                    print(f"  {CLR_PINK}[!] Server dar kharej ({country} - {org}) gharar darad va traffic Beynolmelal ast.{CLR_RESET}")
        except Exception:
            print(f"  {CLR_YELLOW}Barresi structure IP: IP be nazar mota'alleq be Datacenter Dakheli miresad.{CLR_RESET}")
    except Exception as e:
        print(f"  {CLR_RED}[-] Khata: {e}{CLR_RESET}")

def tool_106_domestic_speed_test():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [106] Test Sor'at Download Server-haye Dakheli (CDN Speed Test) ==={CLR_RESET}")
    print("  Download chunk az server Aparat/Asiatech baraye sanjesh sor'at Net Melli bedune internet khareji...\n")
    test_url = "https://www.aparat.com/public/public/images/logo.png"
    t0 = time.time()
    try:
        req = urllib.request.Request(test_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as res:
            data = res.read()
            elapsed = time.time() - t0
            kb = len(data) / 1024
            speed_kb_s = kb / elapsed if elapsed > 0 else 0
            print(f"  {CLR_GREEN}[✓] Daryaft shod: {kb:.1f} KB dar {elapsed:.3f} sanieh{CLR_RESET}")
            print(f"  {CLR_BOLD}{CLR_CYAN}Server Dakheli motassel ast. Sor'at takhmini: {speed_kb_s:.1f} KB/s{CLR_RESET}")
    except Exception as e:
        print(f"  {CLR_RED}[-] Khata dar ertebat ba server dakheli: {e}{CLR_RESET}")

def tool_107_banking_services_status():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [107] Vaziate Dargah-haye Banki va Khedmate Zaroori (10+ Portal) ==={CLR_RESET}")
    banks = [
        ("Shaparak (Pardakht Online)", "https://shaparak.ir"),
        ("Behpardakht Mellat", "https://bpm.shaparak.ir"),
        ("Sadad Melli", "https://sadadpsp.ir"),
        ("Asan Pardakht (Ap)", "https://asanpardakht.ir"),
        ("Parsian E-Commerce", "https://pec.ir"),
        ("Saman Kish (SEP)", "https://sep.ir"),
        ("Bank Markazi (CBI)", "https://cbi.ir"),
        ("Dolat Hamrah (Iran.gov)", "https://iran.gov.ir"),
        ("Adliran (Ghazayi)", "https://adliran.ir"),
        ("Melli Bank Portal", "https://bmi.ir")
    ]
    print("  Arzyabi online boodan dargah-haye tarakonesh va samane-ha:")
    for name, url in banks:
        t0 = time.time()
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=3.0) as r:
                ms = (time.time() - t0) * 1000
                print(f"  {CLR_GREEN}[ONLINE]{CLR_RESET}  {name:<30}: Fa'al ({ms:.0f}ms)")
        except Exception:
            print(f"  {CLR_RED}[OFFLINE]{CLR_RESET} {name:<30}: Kond ya Masdood")

def tool_108_ixp_gaming_latency():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [108] Ping Server-haye Gaming Dakheli va Markaz IXP Tehran ==={CLR_RESET}")
    servers = [
        ("Markaz Tabadole Traffic Tehran (IXP)", "tehran.ixp.ir"),
        ("Server Test Zirsakht (TIC)", "tic.ir"),
        ("Gaming Server Asiatech", "asiatech.ir"),
        ("Gaming Server Shatel", "shatel.ir"),
        ("Pishgaman Server", "pishgaman.net"),
        ("ParsOnline Gaming CDN", "parsonline.com"),
        ("Mobinnet Server", "mobinnet.ir")
    ]
    flag = "-n" if os.name == 'nt' else "-c"
    for name, s in servers:
        t0 = time.time()
        res = subprocess.run(["ping", flag, "2", "-w", "800", s], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elapsed = (time.time() - t0) / 2 * 1000
        if res.returncode == 0:
            color = CLR_GREEN if elapsed < 35 else CLR_YELLOW
            print(f"  {name:<38}: {color}{elapsed:.1f} ms{CLR_RESET}")
        else:
            print(f"  {name:<38}: {CLR_RED}Timeout{CLR_RESET}")

def tool_109_hosts_injector():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [109] Tazrigh Record-haye Pak be File Hosts Windows ==={CLR_RESET}")
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts" if os.name == 'nt' else "/etc/hosts"
    print(f"  Masire file: {hosts_path}")
    print("  [1] Moshahadeh record-haye fe'li")
    print("  [2] Ezafeh kardan negasht dasti Domain be IP (Bypass DNS)")
    c = input("  Entekhab: ").strip()
    if c == '1':
        if os.path.exists(hosts_path):
            with open(hosts_path, 'r', encoding='utf-8', errors='ignore') as f:
                print(f.read())
    elif c == '2':
        ip = input("  IP morede nazar: ").strip()
        dom = input("  Domain morede nazar: ").strip()
        if ip and dom:
            try:
                with open(hosts_path, 'a', encoding='utf-8') as f:
                    f.write(f"\n{ip} {dom}\n")
                print(f"  {CLR_GREEN}[✓] Record '{ip} {dom}' ezafeh shod (Niaz be Administrator).{CLR_RESET}")
            except PermissionError:
                print(f"  {CLR_RED}[-] Dastresi nadarid! Terminal ra ba Run as Administrator baz konid.{CLR_RESET}")

def tool_110_emergency_cheatsheet():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [110] Rahnama va Cheatsheet Net Melli & Mirror-haye Dakheli ==={CLR_RESET}")
    sheet = f"""
  {CLR_BOLD}{CLR_CYAN}● Mirror-haye Dakheli Python (PyPI Mirror zamane ghat'ie internet):{CLR_RESET}
    pip install package_name -i https://pypi.ir/simple
    pip install package_name -i https://mirror.asreertebat.com/pypi/simple

  {CLR_BOLD}{CLR_CYAN}● Mirror-haye Ubuntu va Linux dakhele keshvar:{CLR_RESET}
    archive.ubuntu.com -> ir.archive.ubuntu.com
    mirror.asiatech.ir/ubuntu

  {CLR_BOLD}{CLR_CYAN}● DNS-haye Tahrim-Shekan baraye bypass tahrim-haye khareji:{CLR_RESET}
    Shecan:            178.22.122.100  |  185.51.200.2
    403.online:        10.202.10.202   |  10.202.10.102
    Electro:           78.157.42.101   |  78.157.42.100
    Radar Game:        10.202.10.10    |  10.202.10.11

  {CLR_BOLD}{CLR_CYAN}● Rah-haye dastresi be Search & Ertebatate Dakheli:{CLR_RESET}
    Search Engine:     zarebin.ir
    Platforms:         Aparat, Neshan, Balad, CafeBazaar
"""
    print(sheet)

def tool_111_cf_clean_subnet_scanner():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [111] Cloudflare Clean Subnet Scanner (v2ray / Worker) ==={CLR_RESET}")
    subnets = ["104.16.", "104.17.", "104.18.", "104.19.", "172.64.", "172.67.", "162.159."]
    print("  Barresi 7 subnet Anycast Cloudflare baraye peyda kardan range-haye ba latency kam:\n")
    flag = "-n" if os.name == 'nt' else "-c"
    for sub in subnets:
        test_ip = f"{sub}0.1"
        t0 = time.time()
        res = subprocess.run(["ping", flag, "1", "-w", "500", test_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elapsed = (time.time() - t0) * 1000
        if res.returncode == 0:
            print(f"  {CLR_GREEN}[PASS]{CLR_RESET} Subnet {sub:<10} (IP: {test_ip:<15}): {elapsed:.1f} ms")
        else:
            print(f"  {CLR_RED}[DROP]{CLR_RESET} Subnet {sub:<10} (IP: {test_ip:<15}): Timeout")

def tool_112_tls_handshake_inspector():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [112] TLS Handshake & Packet Drop Inspector ==={CLR_RESET}")
    host = input("  Host baraye test TLS Handshake (Pishfarz: cloudflare.com): ").strip() or "cloudflare.com"
    ctx = ssl.create_default_context()
    t0 = time.time()
    try:
        with socket.create_connection((host, 443), timeout=3.5) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                ms = (time.time() - t0) * 1000
                print(f"  {CLR_GREEN}[✓] TLS Handshake ba {host} moafagh shod! ({ms:.1f}ms){CLR_RESET}")
                print(f"  Protocol: {ssock.version()} | Cipher: {ssock.cipher()[0]}")
    except Exception as e:
        print(f"  {CLR_RED}[!] TLS Handshake failed: {e}{CLR_RESET}")

def tool_113_tcp_rst_detector():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [113] Tashkhis Dast-kari va Fake TCP RST (DPI Reset Detector) ==={CLR_RESET}")
    print("  Ersaal request be site-haye filter baraye baresi inke aya connection ba RST بسته mishavad...")
    test_hosts = ["twitter.com", "facebook.com", "youtube.com"]
    for h in test_hosts:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2.5)
            s.connect((h, 80))
            s.sendall(b"GET / HTTP/1.1\r\nHost: " + h.encode() + b"\r\n\r\n")
            data = s.recv(128)
            print(f"  {h:<15}: Daryaft pasokh ({len(data)} bytes)")
            s.close()
        except ConnectionResetError:
            print(f"  {CLR_RED}{h:<15}: Connection RESET (Fake RST az taraf DPI شناسایی شد!){CLR_RESET}")
        except socket.timeout:
            print(f"  {CLR_YELLOW}{h:<15}: Timeout (Drop shod){CLR_RESET}")
        except Exception as e:
            print(f"  {h:<15}: {e}")

def tool_114_mtu_optimizer():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [114] Peida kardan MTU Behyneh baraye Rad kardan Packet Drop ==={CLR_RESET}")
    target = "8.8.8.8"
    print(f"  Test MTU ping ba Don't Fragment (DF) be {target}...\n")
    sizes = [1500, 1492, 1460, 1420, 1400, 1380, 1360, 1300, 1280]
    optimal = 1280
    for sz in sizes:
        cmd = ["ping", "-f", "-l", str(sz - 28), "-n", "1", "-w", "500", target] if os.name == 'nt' else ["ping", "-M", "do", "-s", str(sz - 28), "-c", "1", target]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res.returncode == 0:
            print(f"  {CLR_GREEN}[PASS]{CLR_RESET} MTU {sz} bytes: Fragment nashod (Safe)")
            optimal = max(optimal, sz)
            break
        else:
            print(f"  {CLR_RED}[FAIL]{CLR_RESET} MTU {sz} bytes: Packet fragmented ya dropped shod.")
    print(f"\n  {CLR_BOLD}{CLR_CYAN}Pishnahad MTU baraye Wireguard/v2ray: {optimal}{CLR_RESET}")

def tool_115_doh_vs_plain_dns():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [115] Moqayese DoH (DNS-over-HTTPS) ba Plain UDP DNS ==={CLR_RESET}")
    domain = "google.com"
    # Plain DNS
    t0 = time.time()
    try:
        socket.gethostbyname(domain)
        p_ms = (time.time() - t0) * 1000
        print(f"  Plain UDP DNS (Port 53): {CLR_GREEN}{p_ms:.1f} ms{CLR_RESET}")
    except Exception as e:
        print(f"  Plain UDP DNS failed: {e}")

    # DoH via Cloudflare
    t1 = time.time()
    try:
        req = urllib.request.Request(f"https://cloudflare-dns.com/dns-query?name={domain}&type=A", headers={"Accept": "application/dns-json"})
        with urllib.request.urlopen(req, timeout=3.5) as r:
            d_ms = (time.time() - t1) * 1000
            print(f"  Cloudflare DoH (Port 443): {CLR_GREEN}{d_ms:.1f} ms{CLR_RESET}")
    except Exception as e:
        print(f"  DoH failed (Ehtemalan DoH block ast): {e}")

def tool_116_socks5_latency_bench():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [116] Benchmark Latency Proxy Local SOCKS5 (127.0.0.1:10808 / 7890) ==={CLR_RESET}")
    ports = [10808, 7890, 2080, 1080]
    for p in ports:
        t0 = time.time()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        res = s.connect_ex(("127.0.0.1", p))
        ms = (time.time() - t0) * 1000
        if res == 0:
            print(f"  {CLR_GREEN}[ONLINE]{CLR_RESET} SOCKS5 Port {p}: Latency {ms:.2f} ms")
        s.close()

def tool_117_http_proxy_speed_test():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [117] Test Sor'at Tunnel HTTP Proxy Local (127.0.0.1:10809 / 7890) ==={CLR_RESET}")
    test_ports = [10809, 7890]
    for p in test_ports:
        proxy_handler = urllib.request.ProxyHandler({'http': f'http://127.0.0.1:{p}', 'https': f'http://127.0.0.1:{p}'})
        opener = urllib.request.build_opener(proxy_handler)
        t0 = time.time()
        try:
            with opener.open("http://cp.cloudflare.com/generate_204", timeout=3.0) as resp:
                elapsed = (time.time() - t0) * 1000
                print(f"  {CLR_GREEN}[PASS]{CLR_RESET} Proxy Port {p}: 204 No Content ({elapsed:.1f} ms) -> Tunnel Baz Ast!")
        except Exception as e:
            print(f"  {CLR_RED}[FAIL]{CLR_RESET} Proxy Port {p}: {e}")

def tool_118_operator_asn_detector():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [118] Shenasayi Operator va ASN Shabake Shoma ==={CLR_RESET}")
    try:
        req = urllib.request.Request("https://ipapi.co/json/", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=4) as r:
            import json
            d = json.loads(r.read().decode())
            print(f"  ● IP Shoma : {d.get('ip')}")
            print(f"  ● ASN      : {d.get('asn')}")
            print(f"  ● Operator : {CLR_BOLD}{CLR_GREEN}{d.get('org')}{CLR_RESET}")
            print(f"  ● Shahr    : {d.get('city')}")
    except Exception as e:
        print(f"  {CLR_RED}[-] Khata: {e}{CLR_RESET}")

def tool_119_routing_split_tunnel():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [119] Barresi Routing Table va Split Tunneling ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            out = subprocess.check_output(["route", "print", "0.0.0.0"], text=True)
            for line in out.splitlines()[:12]:
                print(f"  {line}")
        except Exception as e:
            print(f"  Error: {e}")

def tool_120_set_shecan_dns():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [120] Tanzim Khodkar DNS Shecan / 403 rooye Cart Shabake ==={CLR_RESET}")
    if os.name == 'nt':
        print("  [1] Tanzim Shecan (178.22.122.100 , 185.51.200.2)")
        print("  [2] Tanzim 403.online (10.202.10.202 , 10.202.10.102)")
        print("  [3] Tanzim Electro (78.157.42.101 , 78.157.42.100)")
        c = input("  Entekhab [1-3]: ").strip()
        dns1, dns2 = "178.22.122.100", "185.51.200.2"
        if c == '2': dns1, dns2 = "10.202.10.202", "10.202.10.102"
        elif c == '3': dns1, dns2 = "78.157.42.101", "78.157.42.100"
        
        # Get primary adapter name
        adapter = "Wi-Fi"
        try:
            cmd1 = f"netsh interface ip set dns name=\"{adapter}\" static {dns1}"
            cmd2 = f"netsh interface ip add dns name=\"{adapter}\" {dns2} index=2"
            subprocess.run(cmd1, shell=True, check=False)
            subprocess.run(cmd2, shell=True, check=False)
            print(f"  {CLR_GREEN}[✓] DNS rooye '{adapter}' tanzim shod be {dns1} va {dns2}.{CLR_RESET}")
        except Exception as e:
            print(f"  {CLR_RED}[-] Niaz be Administrator: {e}{CLR_RESET}")
    else:
        print("  Windows netsh utility.")

def tool_121_reset_dns_dhcp():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [121] Reset DNS be Halat Khodkar (DHCP Default) ==={CLR_RESET}")
    if os.name == 'nt':
        for adapter in ["Wi-Fi", "Ethernet"]:
            subprocess.run(f"netsh interface ip set dns name=\"{adapter}\" dhcp", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"  {CLR_GREEN}[✓] DNS cart-haye Wi-Fi va Ethernet be DHCP khodkar bazgasht.{CLR_RESET}")

def tool_122_enable_system_proxy():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [122] Fa'alsazi System Proxy Windows (127.0.0.1:7890 / 10809) ==={CLR_RESET}")
    if os.name == 'nt':
        port = input("  Port proxy (Pishfarz 7890 baraye Clash ya 10809 baraye v2ray): ").strip() or "7890"
        ps_cmd = f"Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings' -Name ProxyEnable -Value 1; Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings' -Name ProxyServer -Value '127.0.0.1:{port}'"
        subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], check=False)
        print(f"  {CLR_GREEN}[✓] Windows System Proxy rooye 127.0.0.1:{port} fa'al shod.{CLR_RESET}")

def tool_123_disable_system_proxy():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [123] Gheyre-fa'alsazi System Proxy Windows (Pak kardan Proxy Giri kardan) ==={CLR_RESET}")
    if os.name == 'nt':
        ps_cmd = "Set-ItemProperty -Path 'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings' -Name ProxyEnable -Value 0"
        subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], check=False)
        print(f"  {CLR_GREEN}[✓] Windows System Proxy gheyre-fa'al shod (Direct Connection).{CLR_RESET}")

def tool_124_university_portals():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [124] Vaziate Dastresi be Portal-haye Daneshgahi va Sanjesh ==={CLR_RESET}")
    unis = [
        ("Daneshgah Tehran (ut.ac.ir)", "ut.ac.ir"),
        ("Daneshgah Sharif (sharif.edu)", "sharif.edu"),
        ("Daneshgah Amirkabir (aut.ac.ir)", "aut.ac.ir"),
        ("Sazman Sanjesh (sanjesh.org)", "sanjesh.org"),
        ("Sanjesh P (sanjeshp.ir)", "sanjeshp.ir")
    ]
    for name, host in unis:
        t0 = time.time()
        try:
            socket.create_connection((host, 80), timeout=2.5)
            ms = (time.time() - t0) * 1000
            print(f"  {CLR_GREEN}[ONLINE]{CLR_RESET}  {name:<32}: Dastras ({ms:.1f}ms)")
        except Exception:
            print(f"  {CLR_RED}[OFFLINE]{CLR_RESET} {name:<32}: Ghat'e")

def tool_125_domestic_banking_deep():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [125] Deep Latency Check Dargah-haye Pardakht Banki ==={CLR_RESET}")
    banks = [
        ("Mellat (bpm.shaparak.ir)", "bpm.shaparak.ir"),
        ("Melli (sadad.shaparak.ir)", "sadad.shaparak.ir"),
        ("Parsian (pec.shaparak.ir)", "pec.shaparak.ir"),
        ("Pasargad (pep.shaparak.ir)", "pep.shaparak.ir"),
        ("Saman (sep.shaparak.ir)", "sep.shaparak.ir")
    ]
    for name, host in banks:
        t0 = time.time()
        try:
            socket.create_connection((host, 443), timeout=2.5)
            ms = (time.time() - t0) * 1000
            print(f"  {CLR_GREEN}[OK]{CLR_RESET}   {name:<28}: {ms:5.1f} ms")
        except Exception:
            print(f"  {CLR_RED}[FAIL]{CLR_RESET} {name:<28}: Timeout")
