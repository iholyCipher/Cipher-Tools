# -*- coding: utf-8 -*-
"""
Cipher Tools - Category 11 Part 2: National Network (Net Melli & Domestic Tools) [Tools 126 - 150]
Architecture: Resilient Diagnostics & Network Telemetry (Fingilish Output for Clean Windows Terminal Display)
"""
import os
import sys
import time
import socket
import ssl
import json
import base64
import urllib.request
import urllib.error
import subprocess

CLR_CYAN = "\033[96m"
CLR_PINK = "\033[95m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_GRAY = "\033[90m"
CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"

def tool_126_domestic_messaging_probe():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [126] Barresi Etesal be Payam-Resanhaye Dakheli ==={CLR_RESET}")
    messengers = [
        ("Bale (bale.ai)", "bale.ai"),
        ("Eitaa (eitaa.com)", "eitaa.com"),
        ("Rubika (rubika.ir)", "rubika.ir"),
        ("Soroush+ (splus.ir)", "splus.ir"),
        ("Gap (gap.im)", "gap.im"),
        ("iGap (igap.net)", "igap.net")
    ]
    for name, host in messengers:
        t0 = time.time()
        try:
            socket.create_connection((host, 443), timeout=2.5)
            ms = (time.time() - t0) * 1000
            print(f"  {CLR_GREEN}[ONLINE]{CLR_RESET}  {name:<25}: Motassel ({ms:.1f}ms)")
        except Exception:
            print(f"  {CLR_RED}[OFFLINE]{CLR_RESET} {name:<25}: Ghat'e ya Dastres-napazir")

def tool_127_global_messaging_probe():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [127] Barresi Vaziate Filtering Payam-Resanhaye Jahani ==={CLR_RESET}")
    globals_apps = [
        ("Telegram (telegram.org)", "telegram.org"),
        ("WhatsApp (whatsapp.com)", "whatsapp.com"),
        ("Instagram (instagram.com)", "instagram.com"),
        ("Twitter/X (x.com)", "x.com"),
        ("Discord (discord.com)", "discord.com"),
        ("YouTube (youtube.com)", "youtube.com"),
        ("Google Play (play.google.com)", "play.google.com")
    ]
    for name, host in globals_apps:
        t0 = time.time()
        try:
            socket.create_connection((host, 443), timeout=2.5)
            ms = (time.time() - t0) * 1000
            print(f"  {CLR_GREEN}[BAZ/MOTASSEL]{CLR_RESET} {name:<30}: Dastras ({ms:.1f}ms)")
        except Exception:
            print(f"  {CLR_RED}[FILTER/BLOCK]{CLR_RESET} {name:<30}: Masdood / Timeout")

def tool_128_vod_streaming_check():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [128] Barresi Sor'at va Dastresi be VOD-haye Dakheli ==={CLR_RESET}")
    vods = [
        ("Filimo (filimo.com)", "filimo.com"),
        ("Namava (namava.ir)", "namava.ir"),
        ("Filmnet (filmnet.ir)", "filmnet.ir"),
        ("Telewebion (telewebion.com)", "telewebion.com"),
        ("Anten (anten.ir)", "anten.ir")
    ]
    for name, host in vods:
        t0 = time.time()
        try:
            socket.create_connection((host, 443), timeout=2.5)
            ms = (time.time() - t0) * 1000
            print(f"  {CLR_GREEN}[OK]{CLR_RESET} {name:<28}: Streaming Active ({ms:.1f}ms)")
        except Exception:
            print(f"  {CLR_RED}[FAIL]{CLR_RESET} {name:<28}: Ghat'e")

def tool_129_domestic_packet_loss():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [129] Test Packet Loss va Stress Shabake Dakheli (20 Packet) ==={CLR_RESET}")
    target = input("  Host baraye test packet loss (Pishfarz: aparat.com): ").strip() or "aparat.com"
    flag = "-n" if os.name == 'nt' else "-c"
    print(f"  {CLR_CYAN}[*] Ersal 20 packet be {target}...{CLR_RESET}")
    res = subprocess.run(["ping", flag, "20", target], stdout=subprocess.PIPE, text=True)
    for line in res.stdout.splitlines():
        if any(k in line.lower() for k in ["loss", "packets", "minimum", "maximum", "average"]):
            print(f"  {CLR_GREEN}{line.strip()}{CLR_RESET}")

def tool_130_git_domestic_mirrors():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [130] Mirror-haye Dakheli Git & Repository ==={CLR_RESET}")
    print("""
  ● Git Mirrors baraye sharayete ghat'ie internet:
    - Gitee (Mirror khedmate open source): gitee.com
    - Gitlab Dakheli: git.ir / git.sharif.edu
    - GitHub Proxy Service: ghproxy.com / kgithub.com
    
    Baraye Clone kardan repo ba proxy mirror:
      git clone https://ghproxy.com/https://github.com/username/repo.git
""")

def tool_131_sni_dpi_inspector():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [131] Test Bazresi SNI va DPI (Deep Packet Inspection) ==={CLR_RESET}")
    host = input("  Host baraye test TLS ClientHello (Pishfarz: youtube.com): ").strip() or "youtube.com"
    print(f"  {CLR_CYAN}[*] Ersal SNI TLS Handshake ba '{host}'...{CLR_RESET}")
    ctx = ssl.create_default_context()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect(("142.250.185.206", 443)) # Google IP
        ss = ctx.wrap_socket(s, server_hostname=host)
        print(f"  {CLR_GREEN}[✓] Handshake moafagh shod. SNI inspection dar in masir filter nakard.{CLR_RESET}")
        ss.close()
    except ssl.SSLError as e:
        print(f"  {CLR_RED}[!] Khata dar SSL: DPI ehtemalan packet SNI ra ghat'e kard: {e}{CLR_RESET}")
    except Exception as e:
        print(f"  {CLR_RED}[!] Etesal bargharar nashod: {e}{CLR_RESET}")

def tool_132_websocket_grpc_prober():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [132] Test Port-haye WebSocket va gRPC (v2ray protocol test) ==={CLR_RESET}")
    test_ip = input("  IP server khareji shoma: ").strip()
    if not test_ip: return
    ports = [80, 443, 8080, 8443, 2053, 2083, 2087, 2096]
    print(f"  Test port-haye CDN WebSocket rooye {test_ip}:")
    for p in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)
        res = s.connect_ex((test_ip, p))
        status = f"{CLR_GREEN}BAZ (OPEN){CLR_RESET}" if res == 0 else f"{CLR_RED}BASTE (FILTER){CLR_RESET}"
        print(f"  Port {p:<5}: {status}")
        s.close()

def tool_133_udp_choking_test():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [133] Test Ekhtelal va Mahdoodiate UDP (UDP Choking Test) ==={CLR_RESET}")
    print("  Barresi inke aya operator traffic UDP ra throttle ya drop mikonad ya kheyr...")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1.5)
    t0 = time.time()
    try:
        # Send DNS query payload to 8.8.8.8
        query = b'\xaa\xbb\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x06google\x03com\x00\x00\x01\x00\x01'
        s.sendto(query, ("8.8.8.8", 53))
        data, _ = s.recvfrom(512)
        ms = (time.time() - t0) * 1000
        print(f"  {CLR_GREEN}[✓] Packet UDP pasokh daryaft kard ({ms:.1f}ms). UDP baz ast.{CLR_RESET}")
    except socket.timeout:
        print(f"  {CLR_RED}[!] UDP Timeout! Operator traffic UDP ra choke/drop mikonad (Moshkel dar WireGuard/Hysteria).{CLR_RESET}")
    except Exception as e:
        print(f"  {CLR_RED}[-] Khata: {e}{CLR_RESET}")
    finally:
        s.close()

def tool_134_hysteria_tuic_prober():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [134] Hysteria / TUIC UDP Port Prober ==={CLR_RESET}")
    ip = input("  IP server Hysteria/TUIC: ").strip()
    port = input("  Port UDP (Pishfarz: 443): ").strip() or "443"
    if not ip: return
    try:
        p = int(port)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(2.0)
        s.sendto(b'\x00' * 16, (ip, p))
        print(f"  {CLR_GREEN}[✓] Packet UDP be {ip}:{p} ersal shod.{CLR_RESET}")
        s.close()
    except Exception as e:
        print(f"  {CLR_RED}[-] Khata: {e}{CLR_RESET}")

def tool_135_wireguard_simulator():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [135] WireGuard Handshake Simulator ==={CLR_RESET}")
    ep = input("  WireGuard Endpoint (IP:Port): ").strip()
    if ":" not in ep: return
    ip, port = ep.split(":", 1)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(2)
        # Wireguard Handshake Initiation message type 1
        dummy_init = b'\x01\x00\x00\x00' + b'\x00' * 144
        s.sendto(dummy_init, (ip, int(port)))
        print(f"  {CLR_CYAN}[*] Initiation packet ersal shod be {ip}:{port}{CLR_RESET}")
        s.close()
    except Exception as e:
        print(f"  {CLR_RED}[-] Khata: {e}{CLR_RESET}")

def tool_136_iran_ntp_sync():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [136] Hamgam-sazi Sa'at ba Server-haye NTP Dakheli ==={CLR_RESET}")
    ntp_servers = ["time.ir", "ntp.day.ir", "0.ir.pool.ntp.org", "time.nist.gov"]
    for s in ntp_servers:
        try:
            ip = socket.gethostbyname(s)
            print(f"  {CLR_GREEN}[OK]{CLR_RESET} NTP Server: {s:<20} -> {ip}")
        except Exception:
            print(f"  {CLR_RED}[FAIL]{CLR_RESET} NTP Server: {s:<20} -> Dastres-napazir")

def tool_137_traceroute_hops():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [137] Traceroute Hops ta Gateway-haye Marzi Keshvar ==={CLR_RESET}")
    target = input("  Host baraye traceroute (Pishfarz: 8.8.8.8): ").strip() or "8.8.8.8"
    cmd = ["tracert", "-d", "-h", "8", "-w", "500", target] if os.name == 'nt' else ["traceroute", "-n", "-m", "8", target]
    print(f"  {CLR_CYAN}[*] Dar hale anjame trace (8 hop avval)...{CLR_RESET}\n")
    subprocess.run(cmd)

def tool_138_national_ip_database():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [138] Este'lam Range IP dar Database CRA (Nim-Baha) ==={CLR_RESET}")
    ip = input("  IP morede nazar: ").strip()
    if not ip: return
    iran_first_octets = {2, 5, 31, 37, 46, 62, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 109, 151, 158, 164, 176, 178, 185, 188, 194, 212, 213, 217}
    try:
        oct1 = int(ip.split(".")[0])
        if oct1 in iran_first_octets:
            print(f"  {CLR_GREEN}[✓] Octet {oct1} dar range alooke shode be Operator-haye Irani ast (Ehtemale bala: Nim-Baha).{CLR_RESET}")
        else:
            print(f"  {CLR_PINK}[!] Octet {oct1} dar range ghalib operator-haye dakheli nist.{CLR_RESET}")
    except Exception:
        print("  Formate IP na-mo'tabar ast.")

def tool_139_dns_leak_checker():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [139] DNS Leak & Gateway Tunnel Leak Detector ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            out = subprocess.check_output(["ipconfig", "/all"], text=True)
            dns_lines = [l.strip() for l in out.splitlines() if "DNS Servers" in l]
            print("  DNS Server-haye tanzim shode rooye cart-haye network:")
            for d in dns_lines:
                print(f"  {CLR_CYAN}➜ {d}{CLR_RESET}")
            print(f"\n  {CLR_YELLOW}Nokte: Agar DNS server-e operator (mesle 192.168.1.1 ya 5.200...) dar halat VPN fa'al bashad, DNS Leak darid.{CLR_RESET}")
        except Exception as e:
            print(f"  Error: {e}")

def tool_140_wlan_reset():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [140] Reset Cart Shabake va Flush DNS Cache ==={CLR_RESET}")
    if os.name == 'nt':
        subprocess.run(["ipconfig", "/flushdns"], stdout=subprocess.DEVNULL)
        subprocess.run(["netsh", "winsock", "reset"], stdout=subprocess.DEVNULL)
        print(f"  {CLR_GREEN}[✓] DNS cache pak shod va Winsock reset gardid.{CLR_RESET}")

def tool_141_pypi_mirror_config():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [141] Tanzim Khodkar Mirror Dakheli PyPI baraye Python ==={CLR_RESET}")
    print("  [1] Set pypi.ir mirror (pip config)")
    print("  [2] Reset be pypi.org pishfarz")
    c = input("  Entekhab [1-2]: ").strip()
    if c == '1':
        subprocess.run(["pip", "config", "set", "global.index-url", "https://pypi.ir/simple"], check=False)
        print(f"  {CLR_GREEN}[✓] Mirror dakheli pypi.ir ba movafaghiyat tanzim shod.{CLR_RESET}")
    elif c == '2':
        subprocess.run(["pip", "config", "unset", "global.index-url"], check=False)
        print(f"  {CLR_GREEN}[✓] Be halat pishfarz bazgasht.{CLR_RESET}")

def tool_142_npm_mirror_config():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [142] Tanzim Khodkar Registry Dakheli NPM (Node.js) ==={CLR_RESET}")
    print("  [1] Set npm mirror dakheli (npm.ir / taobao)")
    print("  [2] Reset be registry.npmjs.org")
    c = input("  Entekhab [1-2]: ").strip()
    if c == '1':
        subprocess.run(["npm", "config", "set", "registry", "https://registry.npmmirror.com"], check=False)
        print(f"  {CLR_GREEN}[✓] Registry npm set shod.{CLR_RESET}")
    elif c == '2':
        subprocess.run(["npm", "config", "set", "registry", "https://registry.npmjs.org"], check=False)
        print(f"  {CLR_GREEN}[✓] Reset shod.{CLR_RESET}")

def tool_143_docker_mirror_guide():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [143] Rahnama va Mirror-haye Dakheli Docker Hub ==={CLR_RESET}")
    print("""
  ● Registry-haye Dakheli Docker dar sharayete Net Melli:
    - Docker IR:      https://docker.ir
    - Docker Asiatech: https://docker.asiatech.ir
    
  Baraye ezafeh kardan be daemon.json (/etc/docker/daemon.json ya Docker Desktop):
    {
      "registry-mirrors": ["https://docker.ir"]
    }
""")

def tool_144_ixp_bgp_summary():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [144] Kholase Masir-dehi BGP va Peering IXP Tehran ==={CLR_RESET}")
    print("""
  ● Marakeze Asli Tabadole Traffic Keshvar (NIXP):
    1. Markaz Emam Khomeini (LCT) - Tehran
    2. Markaz Engelab - Tehran
    3. Markaz Asiatech Azadegan
    4. Markaz Tabriz & Shiraz PoP
    
  Hamayeh operator-ha dar in marakez traffic dakheli ra be soorate mostaghim peere mikonand.
""")

def tool_145_v2ray_config_decoder():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [145] Decoder Link Config-haye v2ray (vmess://, vless://) ==={CLR_RESET}")
    raw_link = input("  Link config ra vared konid (mesle vmess://...): ").strip()
    if raw_link.startswith("vmess://"):
        try:
            b64_part = raw_link[8:]
            decoded = base64.b64decode(b64_part + "==").decode('utf-8', errors='ignore')
            data = json.loads(decoded)
            print(f"\n  {CLR_GREEN}Config VMESS Parse Shod:{CLR_RESET}")
            print(f"  ● Name      : {data.get('ps')}")
            print(f"  ● Address   : {data.get('add')}")
            print(f"  ● Port      : {data.get('port')}")
            print(f"  ● UUID      : {data.get('id')}")
            print(f"  ● Net Type  : {data.get('net')}")
            print(f"  ● Host/SNI  : {data.get('host') or data.get('sni')}")
            print(f"  ● Path      : {data.get('path')}")
            print(f"  ● TLS       : {data.get('tls')}")
        except Exception as e:
            print(f"  {CLR_RED}[-] Khata dar parse vmess: {e}{CLR_RESET}")
    elif raw_link.startswith(("vless://", "trojan://", "ss://")):
        print(f"  {CLR_CYAN}Parsed URI:{CLR_RESET} {raw_link}")
    else:
        print("  Formate link shenakhte nashod.")

def tool_146_sublink_fetcher():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [146] Subscription Link Fetcher & Base64 Config Extractor ==={CLR_RESET}")
    sub_url = input("  Link subscription ra vared konid: ").strip()
    if not sub_url: return
    try:
        req = urllib.request.Request(sub_url, headers={'User-Agent': 'v2rayN/6.23'})
        with urllib.request.urlopen(req, timeout=6) as res:
            content = res.read().decode('utf-8', errors='ignore').strip()
            # Try decode base64
            try:
                decoded = base64.b64decode(content + "==").decode('utf-8', errors='ignore')
                lines = decoded.splitlines()
                print(f"  {CLR_GREEN}[✓] Tedad config-haye daryafti: {len(lines)}{CLR_RESET}")
                for i, l in enumerate(lines[:5], 1):
                    print(f"   [{i}] {l[:65]}...")
                if len(lines) > 5:
                    print(f"   ... va {len(lines) - 5} config digar.")
            except Exception:
                print(f"  Content: {content[:100]}...")
    except Exception as e:
        print(f"  {CLR_RED}[-] Daryafte sublink ba khata movajeh shod: {e}{CLR_RESET}")

def tool_147_cf_clean_ip_pinger():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [147] Ping va Sanjesh Clean IP-haye Cloudflare ==={CLR_RESET}")
    cf_ips = [
        "104.16.0.1", "104.17.0.1", "104.18.0.1", "104.19.0.1", "104.20.0.1",
        "172.64.0.1", "172.67.0.1", "162.159.0.1", "198.41.0.1", "108.162.192.1"
    ]
    print(f"  {CLR_CYAN}[*] Test 10 IP Anycast mashhoor Cloudflare baraye peyda kardan IP pak:{CLR_RESET}\n")
    flag = "-n" if os.name == 'nt' else "-c"
    best = []
    for ip in cf_ips:
        t0 = time.time()
        res = subprocess.run(["ping", flag, "1", "-w", "500", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elapsed = (time.time() - t0) * 1000
        if res.returncode == 0:
            print(f"  {CLR_GREEN}[CLEAN]{CLR_RESET}  {ip:<16}: {elapsed:.1f} ms")
            best.append((ip, elapsed))
        else:
            print(f"  {CLR_RED}[BLOCKED]{CLR_RESET} {ip:<16}: Timeout")
    if best:
        best.sort(key=lambda x: x[1])
        print(f"\n  {CLR_BOLD}{CLR_YELLOW}Behtarin Clean IP: {best[0][0]} ({best[0][1]:.1f}ms){CLR_RESET}")

def tool_148_iran_app_stores():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [148] Barresi Etesal be App Store-haye Irani ==={CLR_RESET}")
    stores = [
        ("Cafe Bazaar (cafebazaar.ir)", "cafebazaar.ir"),
        ("Myket (myket.ir)", "myket.ir"),
        ("Sibapp (sibapp.com)", "sibapp.com"),
        ("Sibche (sibche.com)", "sibche.com")
    ]
    for name, host in stores:
        t0 = time.time()
        try:
            socket.create_connection((host, 443), timeout=2.5)
            ms = (time.time() - t0) * 1000
            print(f"  {CLR_GREEN}[ONLINE]{CLR_RESET}  {name:<30}: Dastras ({ms:.1f}ms)")
        except Exception:
            print(f"  {CLR_RED}[OFFLINE]{CLR_RESET} {name:<30}: Ghat'e")

def tool_149_tcp_optimizer():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [149] Optimize Tanzimate TCP Windows baraye Bypass Packet Loss ==={CLR_RESET}")
    if os.name == 'nt':
        print("  Dastoorate tanzime TCP Auto-Tuning baraye behbood sor'at dar net mokhtal:")
        print(f"  {CLR_CYAN}netsh int tcp set global autotuninglevel=normal{CLR_RESET}")
        print(f"  {CLR_CYAN}netsh int tcp set global congestionprovider=ctcp{CLR_RESET}")
        print(f"  {CLR_CYAN}netsh int tcp set global ecncapability=disabled{CLR_RESET}")
        c = input("\n  Aya mikhahid in tanzimat emal shavad? (y/n): ").strip().lower()
        if c == 'y':
            try:
                subprocess.run(["netsh", "int", "tcp", "set", "global", "autotuninglevel=normal"], check=False)
                subprocess.run(["netsh", "int", "tcp", "set", "global", "ecncapability=disabled"], check=False)
                print(f"  {CLR_GREEN}[✓] Tanzimate TCP ba movafaghiyat optimize shod.{CLR_RESET}")
            except Exception as e:
                print(f"  {CLR_RED}[-] Khata (Niaz be Administrator): {e}{CLR_RESET}")
    else:
        print("  Windows netsh optimization tool.")

def tool_150_emergency_dashboard():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [150] Master Dashboard & Survival Guide Net Melli ==={CLR_RESET}")
    print(f"""
  {CLR_BOLD}{CLR_PINK}===================================================================={CLR_RESET}
  {CLR_BOLD}{CLR_CYAN}       CIPHER TOOLS EMERGENCY NET MELLI SURVIVAL TOOLKIT (50/50){CLR_RESET}
  {CLR_BOLD}{CLR_PINK}===================================================================={CLR_RESET}
  1. Hameye 50 abzar Category 11 fa'al va amadeh be khedmat hastand.
  2. Dar sorate ghat'ie internet:
     - Az abzare [101] vaziat ra check konid.
     - Az abzare [102] behtarin DNS tahrim-shekan (403 ya Shecan) ra peyda konid.
     - Az abzare [104] port-haye local v2ray/Clash ra test konid.
     - Az abzare [147] behtarin Clean IP Cloudflare ra baraye config-ha estekhraj konid.
     - Az abzare [141] mirror dakheli Python ra fa'al konid.
  {CLR_BOLD}{CLR_GREEN}  Stay connected, stay powerful!{CLR_RESET}
""")
