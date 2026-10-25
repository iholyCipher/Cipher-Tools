#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
========================================================================================
                      ⚡ CIPHER TOOLS - CENTURION EDITION (100 TOOLS) ⚡
========================================================================================
Architecture: Modular Enterprise Cybersecurity, Forensics, Networking & System Engineering
Engineered exclusively for: TheCIpher
Platform: Windows x64 / Cross-Platform Ready (Zero External Pip Dependencies)
10 Categories x 10 Tools = 100 Power Modules
========================================================================================
"""

import os
import sys

# Windows UTF-8 stdout fix
try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

# Ensure modules directory is importable
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, "modules"))

from cat1_system import *
from cat2_cpu_mem import *
from cat3_storage import *
from cat4_network import *
from cat5_web import *
from cat6_crypto import *
from cat7_security import *
from cat8_forensics import *
from cat9_windows import *
from cat10_dev import *
from cat11_natnet import *

CLR_CYAN = "\033[96m"
CLR_PINK = "\033[95m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_WHITE = "\033[97m"
CLR_GRAY = "\033[90m"
CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

BANNER = rf"""{CLR_CYAN}
  ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
 ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
 ██║     ██║██████╔╝███████║█████╗  ██████╔╝       ██║   ██║   ██║██║   ██║██║     ███████╗
 ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗       ██║   ██║   ██║██║   ██║██║     ╚════██║
 ╚██████╗██║██║     ██║  ██║███████╗██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
  ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
{CLR_PINK}         >>> CIPHER TOOLS: CENTURION EDITION (100 POWER TOOLS ACTIVATED) <<<{CLR_RESET}
"""

# Master Registry of 100 Tools
TOOLS = {
    # Category 1: System, OS & Kernel
    1: ("OS Architecture & Kernel Build Info", tool_1_os_arch, "System"),
    2: ("Windows Uptime & Boot Time Tracker", tool_2_uptime, "System"),
    3: ("Installed Hotfixes & OS Updates", tool_3_hotfixes, "System"),
    4: ("Environment Variables Explorer", tool_4_env_vars, "System"),
    5: ("System PATH Validator & Missing Path Detector", tool_5_path_validator, "System"),
    6: ("Windows Power Scheme & Battery Status", tool_6_power_scheme, "System"),
    7: ("Active Logged-in Sessions & Users", tool_7_active_sessions, "System"),
    8: ("BIOS / Motherboard Serial & Manufacturer", tool_8_bios_motherboard, "System"),
    9: ("System Locale, Codepage & Timezone", tool_9_locale_timezone, "System"),
    10: ("Windows Shutdown / Reboot Timer", tool_10_shutdown_timer, "System"),

    # Category 2: CPU, Memory & Hardware Benchmarks
    11: ("Multi-Threaded Floating-Point Benchmark (FLOPs)", tool_11_flpop_benchmark, "Hardware"),
    12: ("Single-Thread Integer Math Stress Test", tool_12_int_stress, "Hardware"),
    13: ("RAM Memory Architecture & Capacity", tool_13_ram_capacity, "Hardware"),
    14: ("Real-time CPU Usage Meter (Polled)", tool_14_cpu_usage, "Hardware"),
    15: ("Process Affinity & CPU Core Count Matrix", tool_15_cpu_affinity, "Hardware"),
    16: ("Memory Bandwidth Throughput Test (RAM Speed)", tool_16_ram_throughput, "Hardware"),
    17: ("Top 15 Memory-Consuming Processes", tool_17_top_memory_proc, "Hardware"),
    18: ("Process Killer by PID or Process Name", tool_18_kill_proc, "Hardware"),
    19: ("Process Hierarchy & Parent ID", tool_19_proc_tree, "Hardware"),
    20: ("Real-time System Heartbeat Pulse", tool_20_heartbeat_pulse, "Hardware"),

    # Category 3: Storage, Disk & File System Forensics
    21: ("Partition Capacity & Percentage Bar Graph", tool_21_partition_graph, "Storage"),
    22: ("SHA-256 Duplicate File Finder", tool_22_duplicate_finder, "Storage"),
    23: ("Recursive Directory Space Consumption Tree", tool_23_folder_tree, "Storage"),
    24: ("Ghost Folder Pruner (Empty Directory Eraser)", tool_24_empty_pruner, "Storage"),
    25: ("Smart Archive Search, Auto-Extract & Explorer Launch", tool_25_archive_extractor, "Storage"),
    26: ("Batch File Extension Renamer", tool_26_batch_rename, "Storage"),
    27: ("Checksum Manifest Creator (.sha256)", tool_27_create_checksum, "Storage"),
    28: ("Checksum Manifest Verifier", tool_28_verify_checksum, "Storage"),
    29: ("Zero-Byte / Corrupted File Finder", tool_29_zero_byte_finder, "Storage"),
    30: ("Largest Files Finder in Target Directory", tool_30_largest_files, "Storage"),

    # Category 4: Network Reconnaissance & Diagnostics
    31: ("Local Subnet ARP & Active Host Sweep", tool_31_arp_sweep, "Network"),
    32: ("TCP Port Scanner (Common Services)", tool_32_port_scanner, "Network"),
    33: ("Ping Latency & Packet Loss Analyzer", tool_33_ping_analyzer, "Network"),
    34: ("DNS Jitter & Multi-Provider Benchmark", tool_34_dns_jitter, "Network"),
    35: ("Network Interface Adapters & MAC Address Matrix", tool_35_net_adapters, "Network"),
    36: ("Active TCP/UDP Connections Inspector (Netstat)", tool_36_active_conns, "Network"),
    37: ("Default Gateway & Routing Table Checker", tool_37_gateway_route, "Network"),
    38: ("Hostname to IP / Reverse DNS Lookup", tool_38_reverse_dns, "Network"),
    39: ("Local Hostname Resolution & Hosts File Viewer", tool_39_hosts_file, "Network"),
    40: ("WiFi Profile & Signal Inspector (netsh wlan)", tool_40_wifi_profiles, "Network"),

    # Category 5: Web & Internet Intelligence
    41: ("Public IP, Geolocation & ISP Telemetry", tool_41_public_ip, "Web"),
    42: ("HTTP/HTTPS Header & Server Banner Grabber", tool_42_headers_grabber, "Web"),
    43: ("Website SSL/TLS Certificate Expiration Checker", tool_43_ssl_cert, "Web"),
    44: ("Website Response Time & Status Code Prober", tool_44_status_prober, "Web"),
    45: ("Fast URL Downloader (CLI Wget style)", tool_45_url_downloader, "Web"),
    46: ("Robots.txt & Sitemap Fetcher", tool_46_robots_fetcher, "Web"),
    47: ("URL Expander (Follow Redirect Chains)", tool_47_redirect_chain, "Web"),
    48: ("HTML Title & Meta Tags Extractor", tool_48_meta_extractor, "Web"),
    49: ("Domain Whois & Registrar Probe", tool_49_domain_whois, "Web"),
    50: ("Internet Connectivity Continuous Monitor", tool_50_connectivity_monitor, "Web"),

    # Category 6: Cryptography, Hashes & Ciphers
    51: ("Multi-Hash Calculator (MD5, SHA1, SHA256, SHA512)", tool_51_multi_hash, "Crypto"),
    52: ("Hash Type Algorithmic Identifier", tool_52_hash_ident, "Crypto"),
    53: ("Symmetric XOR Stream Cipher", tool_53_xor_cipher, "Crypto"),
    54: ("Base16 (Hex), Base32 & Base64 Encoder/Decoder", tool_54_base_encoders, "Crypto"),
    55: ("Caesar / ROT13 Substitution Cipher", tool_55_caesar_rot13, "Crypto"),
    56: ("High-Entropy Password & Token Matrix", tool_56_password_matrix, "Crypto"),
    57: ("Shannon Entropy Password Strength Grader", tool_57_shannon_entropy, "Crypto"),
    58: ("HMAC SHA-256 Signature Generator", tool_58_hmac_generator, "Crypto"),
    59: ("Secure Random Number / Dice Generator", tool_59_random_dice, "Crypto"),
    60: ("UUID / GUID Generator (v4 Cryptographic)", tool_60_uuid_gen, "Crypto"),

    # Category 7: Cybersecurity, Defense & Sanitization
    61: ("DoD 5220.22-M 3-Pass Military File Shredder", tool_61_shredder, "Security"),
    62: ("Free Space Zero-Fill Wiper (Anti-Forensics)", tool_62_zero_fill, "Security"),
    63: ("Windows Clipboard Security Sanitizer", tool_63_clipboard_wipe, "Security"),
    64: ("Windows Temp & Crash Dump Purger", tool_64_temp_purger, "Security"),
    65: ("Browser Cache Cleaner Helper", tool_65_browser_cache, "Security"),
    66: ("Suspicious Hidden File (.exe/.dll in AppData) Detector", tool_66_hidden_exe, "Security"),
    67: ("USB Drive Autorun & Shortcut Virus Scanner", tool_67_usb_autorun, "Security"),
    68: ("NTFS Alternate Data Stream (ADS) Detector", tool_68_ntfs_ads, "Security"),
    69: ("Windows Firewall Status & Profile Inspector", tool_69_firewall_status, "Security"),
    70: ("User Account Control (UAC) Elevation Level Checker", tool_70_uac_level, "Security"),

    # Category 8: Binary Forensics & Reverse Engineering
    71: ("Binary Hex Viewer (Hex Dump with ASCII column)", tool_71_hex_viewer, "Forensics"),
    72: ("Magic Bytes / File Header Signature Identifier", tool_72_magic_bytes, "Forensics"),
    73: ("ASCII & Unicode String Extractor", tool_73_string_extract, "Forensics"),
    74: ("PE Executable Header & Section Analyzer", tool_74_pe_header, "Forensics"),
    75: ("File Entropy Calculator (Packed / Encrypted Binary)", tool_75_file_entropy, "Forensics"),
    76: ("Binary Difference Comparator (Byte-by-byte diff)", tool_76_binary_diff, "Forensics"),
    77: ("Base64 Extractor from Binary Data", tool_77_base64_in_binary, "Forensics"),
    78: ("IP / URL Regex Finder in Binary Files", tool_78_ip_regex_scanner, "Forensics"),
    79: ("File Timestamp Forgery / Timestomp Detector", tool_79_timestomp_check, "Forensics"),
    80: ("File MIME Type Guessing Engine", tool_80_mime_guess, "Forensics"),

    # Category 9: Windows Administration & Registry
    81: ("Windows Startup Items & Registry Run Keys", tool_81_startup_items, "Windows"),
    82: ("Windows Services Inspector & Status Query", tool_82_services_status, "Windows"),
    83: ("Windows Event Viewer Critical Errors Log", tool_83_event_errors, "Windows"),
    84: ("Installed Software & Programs Inventory", tool_84_installed_apps, "Windows"),
    85: ("Windows Defender Anti-Malware Engine Status", tool_85_defender_status, "Windows"),
    86: ("DNS Cache Flush Utility (ipconfig /flushdns)", tool_86_flush_dns, "Windows"),
    87: ("Task Scheduler Active Jobs Query", tool_87_task_scheduler, "Windows"),
    88: ("Windows Product Key / Digital License Query", tool_88_product_key, "Windows"),
    89: ("System File Integrity Checker (SFC helper)", tool_89_sfc_helper, "Windows"),
    90: ("Windows Update Service State Inspector", tool_90_windows_update, "Windows"),

    # Category 10: Productivity, Converters & Developer Utilities
    91: ("Unix Epoch Timestamp Converter", tool_91_unix_epoch, "Dev"),
    92: ("JSON Pretty Printer & Syntax Validator", tool_92_json_formatter, "Dev"),
    93: ("XML / HTML Tag Stripper", tool_93_xml_formatter, "Dev"),
    94: ("IP Subnet Mask & CIDR Calculator", tool_94_cidr_calc, "Dev"),
    95: ("Number Base Converter (Bin, Oct, Dec, Hex)", tool_95_base_converter, "Dev"),
    96: ("Text Word, Line & Character Counter", tool_96_word_counter, "Dev"),
    97: ("Text Case Converter (camel, snake, kebab)", tool_97_case_converter, "Dev"),
    98: ("Markdown to Plain Text Stripper", tool_98_markdown_strip, "Dev"),
    99: ("Regex Pattern Matcher & Tester", tool_99_regex_tester, "Dev"),
    100: ("Developer Scratchpad & Quick Note Vault", tool_100_scratch_vault, "Dev"),

    # Category 11: National Network (Net Melli & Domestic Tools) [50 Tools: 101 - 150]
    101: ("Tashkhise Vaziate Shabake (Net Melli vs Internet Beynolmelal)", tool_101_netmelli_checker, "NatNet"),
    102: ("Massive DNS Benchmark (26 DNS: Shecan, 403, Electro, Radar)", tool_102_iran_dns_benchmark, "NatNet"),
    103: ("Shekarchi Aloudegi va DNS Poisoning (Fake 10.10.34.34 Detector)", tool_103_dns_poison_detector, "NatNet"),
    104: ("Massive VPN & Proxy Core Port Scanner (45+ Ports)", tool_104_proxy_health_check, "NatNet"),
    105: ("Barresi Traffic Dakheli va Nim-Baha (Domestic IP Inspector)", tool_105_domestic_ip_inspector, "NatNet"),
    106: ("Test Sor'at Download Server-haye Dakheli (CDN Speed Test)", tool_106_domestic_speed_test, "NatNet"),
    107: ("Vaziate Dargah-haye Banki & Khedmate Zaroori (10+ Portal)", tool_107_banking_services_status, "NatNet"),
    108: ("Ping Server-haye Gaming Dakheli va IXP Tehran", tool_108_ixp_gaming_latency, "NatNet"),
    109: ("Tazrigh Record-haye Pak be File Hosts Windows (Bypass DNS)", tool_109_hosts_injector, "NatNet"),
    110: ("Rahnama & Cheatsheet Net Melli & Mirror-haye Dakheli (PyPI, Ubuntu)", tool_110_emergency_cheatsheet, "NatNet"),
    111: ("Cloudflare Clean Subnet Scanner (v2ray / Worker)", tool_111_cf_clean_subnet_scanner, "NatNet"),
    112: ("TLS Handshake & Packet Drop Inspector", tool_112_tls_handshake_inspector, "NatNet"),
    113: ("Tashkhis Dast-kari va Fake TCP RST (DPI Reset Detector)", tool_113_tcp_rst_detector, "NatNet"),
    114: ("Peida kardan MTU Behyneh baraye Rad kardan Packet Drop", tool_114_mtu_optimizer, "NatNet"),
    115: ("Moqayese DoH (DNS-over-HTTPS) ba Plain UDP DNS", tool_115_doh_vs_plain_dns, "NatNet"),
    116: ("Benchmark Latency Proxy Local SOCKS5 (127.0.0.1:10808 / 7890)", tool_116_socks5_latency_bench, "NatNet"),
    117: ("Test Sor'at Tunnel HTTP Proxy Local (127.0.0.1:10809 / 7890)", tool_117_http_proxy_speed_test, "NatNet"),
    118: ("Shenasayi Operator va ASN Shabake Shoma", tool_118_operator_asn_detector, "NatNet"),
    119: ("Barresi Routing Table va Split Tunneling", tool_119_routing_split_tunnel, "NatNet"),
    120: ("Tanzim Khodkar DNS Shecan / 403 rooye Cart Shabake", tool_120_set_shecan_dns, "NatNet"),
    121: ("Reset DNS be Halat Khodkar (DHCP Default)", tool_121_reset_dns_dhcp, "NatNet"),
    122: ("Fa'alsazi System Proxy Windows (127.0.0.1:7890 / 10809)", tool_122_enable_system_proxy, "NatNet"),
    123: ("Gheyre-fa'alsazi System Proxy Windows (Pak kardan Proxy)", tool_123_disable_system_proxy, "NatNet"),
    124: ("Vaziate Dastresi be Portal-haye Daneshgahi va Sanjesh", tool_124_university_portals, "NatNet"),
    125: ("Deep Latency Check Dargah-haye Pardakht Banki", tool_125_domestic_banking_deep, "NatNet"),
    126: ("Barresi Etesal be Payam-Resanhaye Dakheli (Bale, Eitaa, Rubika)", tool_126_domestic_messaging_probe, "NatNet"),
    127: ("Barresi Vaziate Filtering Payam-Resanhaye Jahani (Telegram, X)", tool_127_global_messaging_probe, "NatNet"),
    128: ("Barresi Sor'at va Dastresi be VOD-haye Dakheli (Filimo, Namava)", tool_128_vod_streaming_check, "NatNet"),
    129: ("Test Packet Loss va Stress Shabake Dakheli (20 Packet)", tool_129_domestic_packet_loss, "NatNet"),
    130: ("Mirror-haye Dakheli Git & Repository", tool_130_git_domestic_mirrors, "NatNet"),
    131: ("Test Bazresi SNI va DPI (Deep Packet Inspection)", tool_131_sni_dpi_inspector, "NatNet"),
    132: ("Test Port-haye WebSocket va gRPC (v2ray protocol test)", tool_132_websocket_grpc_prober, "NatNet"),
    133: ("Test Ekhtelal va Mahdoodiate UDP (UDP Choking Test)", tool_133_udp_choking_test, "NatNet"),
    134: ("Hysteria / TUIC UDP Port Prober", tool_134_hysteria_tuic_prober, "NatNet"),
    135: ("WireGuard Handshake Simulator", tool_135_wireguard_simulator, "NatNet"),
    136: ("Hamgam-sazi Sa'at ba Server-haye NTP Dakheli", tool_136_iran_ntp_sync, "NatNet"),
    137: ("Traceroute Hops ta Gateway-haye Marzi Keshvar", tool_137_traceroute_hops, "NatNet"),
    138: ("Este'lam Range IP dar Database CRA (Nim-Baha)", tool_138_national_ip_database, "NatNet"),
    139: ("DNS Leak & Gateway Tunnel Leak Detector", tool_139_dns_leak_checker, "NatNet"),
    140: ("Reset Cart Shabake va Flush DNS Cache", tool_140_wlan_reset, "NatNet"),
    141: ("Tanzim Khodkar Mirror Dakheli PyPI baraye Python", tool_141_pypi_mirror_config, "NatNet"),
    142: ("Tanzim Khodkar Registry Dakheli NPM (Node.js)", tool_142_npm_mirror_config, "NatNet"),
    143: ("Rahnama va Mirror-haye Dakheli Docker Hub", tool_143_docker_mirror_guide, "NatNet"),
    144: ("Kholase Masir-dehi BGP va Peering IXP Tehran", tool_144_ixp_bgp_summary, "NatNet"),
    145: ("Decoder Link Config-haye v2ray (vmess://, vless://)", tool_145_v2ray_config_decoder, "NatNet"),
    146: ("Subscription Link Fetcher & Base64 Config Extractor", tool_146_sublink_fetcher, "NatNet"),
    147: ("Ping va Sanjesh Clean IP-haye Cloudflare", tool_147_cf_clean_ip_pinger, "NatNet"),
    148: ("Barresi Etesal be App Store-haye Irani", tool_148_iran_app_stores, "NatNet"),
    149: ("Optimize Tanzimate TCP Windows baraye Bypass Packet Loss", tool_149_tcp_optimizer, "NatNet"),
    150: ("Master Dashboard & Survival Guide Net Melli (50/50)", tool_150_emergency_dashboard, "NatNet")
}

CATEGORIES = [
    ("System, OS & Kernel", 1, 10),
    ("CPU, Memory & Hardware Benchmarks", 11, 20),
    ("Storage, Disk & File System Forensics", 21, 30),
    ("Network Reconnaissance & Diagnostics", 31, 40),
    ("Web & Internet Intelligence", 41, 50),
    ("Cryptography, Hashes & Ciphers", 51, 60),
    ("Cybersecurity, Defense & Sanitization", 61, 70),
    ("Binary Forensics & Reverse Engineering", 71, 80),
    ("Windows Administration & Registry", 81, 90),
    ("Productivity, Converters & Developer Utilities", 91, 100),
    ("National Network (Net Melli & Domestic Tools)", 101, 150),
]

def pause():
    input(f"\n{CLR_GRAY}Press Enter to continue...{CLR_RESET}")

def run_tool(num):
    if num in TOOLS:
        name, func, cat = TOOLS[num]
        try:
            func()
        except Exception as e:
            print(f"\n{CLR_RED}[-] Tool Execution Error: {e}{CLR_RESET}")
        pause()
    else:
        print(f"{CLR_RED}[-] Invalid tool number [{num}]. Valid range: 1 to {len(TOOLS)}.{CLR_RESET}")
        pause()

def view_category(cat_idx):
    cat_name, start_id, end_id = CATEGORIES[cat_idx]
    clear_screen()
    print(BANNER)
    print(f" {CLR_BOLD}{CLR_YELLOW}=== [ CATEGORY {cat_idx+1}: {cat_name.upper()} ] ==={CLR_RESET}\n")
    for tid in range(start_id, end_id + 1):
        name, _, _ = TOOLS[tid]
        print(f"  {CLR_CYAN}[{tid:<3}]{CLR_RESET} {name}")
    print(f"\n  {CLR_GRAY}[0] Back to Main Menu{CLR_RESET}")
    
    c = input(f"\n {CLR_YELLOW}Select Tool [{start_id}-{end_id}] or 0: {CLR_RESET}").strip()
    if c.isdigit():
        num = int(c)
        if start_id <= num <= end_id:
            run_tool(num)

def search_tools():
    clear_screen()
    print(BANNER)
    q = input(f" {CLR_YELLOW}Enter search keyword across all 100 tools: {CLR_RESET}").strip().lower()
    if not q: return
    
    matches = []
    for tid, (name, _, cat) in TOOLS.items():
        if q in name.lower() or q in cat.lower():
            matches.append((tid, name, cat))
            
    print(f"\n {CLR_GREEN}[✓] Discovered {len(matches)} matching tool(s):{CLR_RESET}\n")
    for tid, name, cat in matches:
        print(f"  {CLR_CYAN}[{tid:<3}]{CLR_RESET} {name} {CLR_GRAY}({cat}){CLR_RESET}")
        
    sel = input(f"\n {CLR_YELLOW}Enter Tool ID to execute (or Enter to cancel): {CLR_RESET}").strip()
    if sel.isdigit() and int(sel) in TOOLS:
        run_tool(int(sel))

def display_all_tools():
    clear_screen()
    print(BANNER)
    print(f" {CLR_BOLD}{CLR_PINK}>>> ALL 150 CIPHER TOOLS DIRECTORY <<<{CLR_RESET}\n")
    for cat_idx, (cat_name, start_id, end_id) in enumerate(CATEGORIES, 1):
        print(f" {CLR_BOLD}{CLR_YELLOW}[C{cat_idx}] {cat_name}{CLR_RESET}")
        for tid in range(start_id, end_id + 1):
            name, _, _ = TOOLS[tid]
            print(f"   {CLR_CYAN}[{tid:<3}]{CLR_RESET} {name}")
        print()
    pause()

def main():
    while True:
        clear_screen()
        print(BANNER)
        print(f" {CLR_BOLD}{CLR_WHITE}TITAN CATEGORY DIRECTORY (150 TOTAL TOOLS):{CLR_RESET}")
        for idx, (cat_name, s, e) in enumerate(CATEGORIES, 1):
            print(f"  {CLR_CYAN}[C{idx:<2}]{CLR_RESET} {cat_name:<48} {CLR_GRAY}[Tools {s:02d}-{e:03d}]{CLR_RESET}")
            
        print(f"\n {CLR_BOLD}{CLR_WHITE}QUICK ACTIONS:{CLR_RESET}")
        print(f"  {CLR_PINK}[1-150]{CLR_RESET} Type any Tool Number directly to launch")
        print(f"  {CLR_PINK}[S]{CLR_RESET}     Search all 150 tools by keyword")
        print(f"  {CLR_PINK}[A]{CLR_RESET}     Display full catalog of all 150 tools")
        print(f"  {CLR_RED}[0]{CLR_RESET}     Exit Cipher Tools\n")

        raw = input(f" {CLR_YELLOW}TheCIpher@titan:~$ {CLR_RESET}").strip()
        if not raw:
            continue
            
        cmd = raw.lower()
        if cmd == '0' or cmd == 'exit' or cmd == 'quit':
            clear_screen()
            print(f"\n{CLR_GREEN}Cipher Tools Centurion terminated safely. Have a great day, TheCIpher!{CLR_RESET}\n")
            break
        elif cmd == 's':
            search_tools()
        elif cmd == 'a':
            display_all_tools()
        elif cmd.startswith('c') and cmd[1:].isdigit():
            cnum = int(cmd[1:]) - 1
            if 0 <= cnum < len(CATEGORIES):
                view_category(cnum)
        elif cmd.isdigit():
            tnum = int(cmd)
            if 1 <= tnum <= len(TOOLS):
                run_tool(tnum)
            elif 1 <= tnum <= len(CATEGORIES):
                view_category(tnum - 1)
        else:
            print(f" {CLR_RED}[-] Unknown command or tool ID.{CLR_RESET}")
            pause()

if __name__ == "__main__":
    main()
