# -*- coding: utf-8 -*-
"""
Cipher Tools - Category 5: Web & Internet Intelligence (Tools 41 - 50)
"""
import os
import sys
import time
import json
import ssl
import socket
import urllib.request
import urllib.error

CLR_CYAN = "\033[96m"
CLR_PINK = "\033[95m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_GRAY = "\033[90m"
CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"

def tool_41_public_ip():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [41] Public IP & Geolocation Telemetry ==={CLR_RESET}")
    try:
        req = urllib.request.Request("https://ipapi.co/json/", headers={'User-Agent': 'CipherTools/3.0'})
        with urllib.request.urlopen(req, timeout=5) as res:
            d = json.loads(res.read().decode())
            print(f"  {CLR_GREEN}● Public IP:{CLR_RESET}   {d.get('ip')}")
            print(f"  {CLR_GREEN}● Country  :{CLR_RESET}   {d.get('country_name')} ({d.get('region')})")
            print(f"  {CLR_GREEN}● City     :{CLR_RESET}   {d.get('city')}")
            print(f"  {CLR_GREEN}● ISP / Org:{CLR_RESET}   {d.get('org')}")
    except Exception as e:
        print(f"  {CLR_RED}[-] Error: {e}{CLR_RESET}")

def tool_42_headers_grabber():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [42] HTTP/HTTPS Header & Server Banner Grabber ==={CLR_RESET}")
    url = input("  Enter target URL (e.g. https://example.com): ").strip()
    if not url.startswith("http"): url = "https://" + url
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=6) as res:
            for k, v in res.headers.items():
                print(f"  {CLR_GREEN}{k:<20}:{CLR_RESET} {v}")
    except Exception as e:
        print(f"  {CLR_RED}[-] Request failed: {e}{CLR_RESET}")

def tool_43_ssl_cert():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [43] Website SSL/TLS Certificate Inspector ==={CLR_RESET}")
    host = input("  Enter domain (e.g. google.com): ").strip()
    ctx = ssl.create_default_context()
    try:
        with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
            s.settimeout(5)
            s.connect((host, 443))
            cert = s.getpeercert()
            print(f"  Subject: {cert.get('subject')}")
            print(f"  Issuer : {cert.get('issuer')}")
            print(f"  Valid Until: {cert.get('notAfter')}")
    except Exception as e:
        print(f"  {CLR_RED}[-] SSL query error: {e}{CLR_RESET}")

def tool_44_status_prober():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [44] Website Response Time & Status Code Prober ==={CLR_RESET}")
    url = input("  Enter URL: ").strip()
    if not url.startswith("http"): url = "https://" + url
    t0 = time.time()
    try:
        with urllib.request.urlopen(url, timeout=6) as res:
            el = (time.time() - t0) * 1000
            print(f"  {CLR_GREEN}[✓] Status Code: {res.status} OK ({el:.1f} ms){CLR_RESET}")
    except urllib.error.HTTPError as he:
        print(f"  {CLR_YELLOW}[!] Status Code: {he.code}{CLR_RESET}")
    except Exception as e:
        print(f"  {CLR_RED}[-] Prober error: {e}{CLR_RESET}")

def tool_45_url_downloader():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [45] Fast URL File Downloader ==={CLR_RESET}")
    url = input("  Enter direct download link: ").strip()
    if not url: return
    fname = url.split("/")[-1].split("?")[0] or "downloaded_file"
    dest = os.path.join(os.path.expanduser("~"), "Downloads", fname)
    print(f"  Downloading to {dest}...")
    try:
        urllib.request.urlretrieve(url, dest)
        print(f"  {CLR_GREEN}[✓] Downloaded successfully! ({os.path.getsize(dest):,} bytes){CLR_RESET}")
    except Exception as e:
        print(f"  {CLR_RED}[-] Download failed: {e}{CLR_RESET}")

def tool_46_robots_fetcher():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [46] Robots.txt Fetcher ==={CLR_RESET}")
    domain = input("  Enter domain (e.g. wikipedia.org): ").strip()
    url = f"https://{domain}/robots.txt"
    try:
        with urllib.request.urlopen(url, timeout=5) as res:
            lines = res.read().decode('utf-8', errors='ignore').splitlines()
            print(f"  Fetched {len(lines)} lines from {url}:")
            for l in lines[:15]: print(f"  {l}")
    except Exception as e:
        print(f"  {CLR_RED}[-] Could not fetch robots.txt: {e}{CLR_RESET}")

def tool_47_redirect_chain():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [47] URL Expander & Redirect Tracker ==={CLR_RESET}")
    url = input("  Enter shortened URL: ").strip()
    if not url.startswith("http"): url = "https://" + url
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=6) as res:
            print(f"  {CLR_GREEN}Final Destination URL:{CLR_RESET} {res.geturl()}")
    except Exception as e:
        print(f"  {CLR_RED}[-] Trace error: {e}{CLR_RESET}")

def tool_48_meta_extractor():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [48] HTML Title & Meta Tags Extractor ==={CLR_RESET}")
    url = input("  Enter website URL: ").strip()
    if not url.startswith("http"): url = "https://" + url
    try:
        with urllib.request.urlopen(url, timeout=5) as res:
            html = res.read().decode('utf-8', errors='ignore')
            import re
            m = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
            print(f"  {CLR_GREEN}Page Title:{CLR_RESET} {m.group(1) if m else 'None found'}")
    except Exception as e:
        print(f"  {CLR_RED}[-] Error: {e}{CLR_RESET}")

def tool_49_domain_whois():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [49] Domain Whois / IP Resolution ==={CLR_RESET}")
    d = input("  Enter domain name: ").strip()
    try:
        ip = socket.gethostbyname(d)
        print(f"  Resolved IP: {ip}")
    except Exception as e:
        print(f"  {CLR_RED}[-] Resolution error: {e}{CLR_RESET}")

def tool_50_connectivity_monitor():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [50] Internet Connectivity Pulse (5 probes) ==={CLR_RESET}")
    for i in range(5):
        t0 = time.time()
        try:
            socket.create_connection(("1.1.1.1", 53), timeout=2)
            el = (time.time() - t0) * 1000
            print(f"  [{i+1}/5] {CLR_GREEN}ONLINE{CLR_RESET} - Cloudflare latency: {el:.1f}ms")
        except Exception:
            print(f"  [{i+1}/5] {CLR_RED}OFFLINE{CLR_RESET}")
        time.sleep(0.5)
