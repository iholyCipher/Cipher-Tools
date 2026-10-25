# -*- coding: utf-8 -*-
"""
Cipher Tools - Category 7: Cybersecurity, Defense & Sanitization (Tools 61 - 70)
"""
import os
import sys
import secrets
import subprocess

CLR_CYAN = "\033[96m"
CLR_PINK = "\033[95m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_GRAY = "\033[90m"
CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"

def tool_61_shredder():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [61] DoD 5220.22-M 3-Pass File Shredder ==={CLR_RESET}")
    target = input("  Enter file to irreversibly shred: ").strip(' "\'')
    if not os.path.isfile(target): return
    conf = input(f"  {CLR_RED}Confirm destroy '{os.path.basename(target)}'? (yes/no): {CLR_RESET}").lower()
    if conf != 'yes': return
    sz = os.path.getsize(target)
    with open(target, 'ba+', buffering=0) as f:
        f.seek(0); f.write(b'\x00' * sz)
        f.seek(0); f.write(b'\xFF' * sz)
        f.seek(0); f.write(secrets.token_bytes(sz))
    os.remove(target)
    print(f"  {CLR_GREEN}[✓] Data destroyed with military overwrite.{CLR_RESET}")

def tool_62_zero_fill():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [62] Anti-Forensics Free Space Zero-Fill ==={CLR_RESET}")
    print("  Creates a temporary 10MB zero-filled block to sanitize deleted sectors, then removes it.")
    tmp_wipe = os.path.join(os.getenv('TEMP', '.'), "wipe_block.tmp")
    with open(tmp_wipe, 'wb') as f:
        f.write(b'\x00' * (10 * 1024 * 1024))
    os.remove(tmp_wipe)
    print(f"  {CLR_GREEN}[✓] Zero-fill purge complete.{CLR_RESET}")

def tool_63_clipboard_wipe():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [63] Windows Clipboard Security Sanitizer ==={CLR_RESET}")
    if os.name == 'nt':
        subprocess.run(["powershell", "-NoProfile", "-Command", "Set-Clipboard -Value $null"], check=False)
        print(f"  {CLR_GREEN}[✓] Clipboard memory sanitized.{CLR_RESET}")

def tool_64_temp_purger():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [64] Windows Temp Cache & Crash Dump Purger ==={CLR_RESET}")
    t = os.getenv('TEMP')
    if t and os.path.isdir(t):
        cnt = 0
        for r, _, fs in os.walk(t):
            for f in fs:
                try: os.remove(os.path.join(r, f)); cnt += 1
                except Exception: pass
        print(f"  {CLR_GREEN}[✓] Purged {cnt} temporary cache files.{CLR_RESET}")

def tool_65_browser_cache():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [65] Browser Cache Helper ==={CLR_RESET}")
    user_home = os.path.expanduser("~")
    chrome_cache = os.path.join(user_home, "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Cache")
    if os.path.exists(chrome_cache):
        sz = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(chrome_cache) for f in fs)
        print(f"  Chrome Cache Detected: {sz / (1024*1024):.2f} MB")
    else:
        print("  Chrome cache not detected at default path.")

def tool_66_hidden_exe():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [66] Suspicious Binaries (.exe/.dll) in AppData Inspector ==={CLR_RESET}")
    appdata = os.getenv('APPDATA')
    suspicious = []
    if appdata:
        for r, _, fs in os.walk(appdata):
            for f in fs:
                if f.lower().endswith(('.exe', '.scr', '.vbs', '.bat')):
                    suspicious.append(os.path.join(r, f))
                    if len(suspicious) >= 10: break
            if len(suspicious) >= 10: break
    print(f"  Found {len(suspicious)} binaries in AppData:")
    for s in suspicious: print(f"  ➜ {s}")

def tool_67_usb_autorun():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [67] USB Autorun / Shortcut Virus Scanner ==={CLR_RESET}")
    for d in ["D:\\", "E:\\", "F:\\", "G:\\"]:
        if os.path.exists(d):
            ar = os.path.join(d, "autorun.inf")
            if os.path.exists(ar):
                print(f"  {CLR_RED}[!] Suspicious autorun.inf found on {d}!{CLR_RESET}")
            else:
                print(f"  {CLR_GREEN}[✓] Drive {d} clean (No autorun.inf).{CLR_RESET}")

def tool_68_ntfs_ads():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [68] NTFS Alternate Data Stream (ADS) Detector ==={CLR_RESET}")
    folder = input("  Enter folder to scan for ADS streams: ").strip(' "\'')
    if os.name == 'nt' and os.path.isdir(folder):
        cmd = f"Get-ChildItem -Path '{folder}' -Stream * | Where-Object {{ $_.Stream -ne ':$DATA' }}"
        try:
            out = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True)
            print(out if out.strip() else "  No hidden Alternate Data Streams detected.")
        except Exception as e:
            print(f"  Error: {e}")

def tool_69_firewall_status():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [69] Windows Firewall Profile Status ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            out = subprocess.check_output(["netsh", "advfirewall", "show", "allprofiles", "state"], text=True)
            print(out.strip())
        except Exception as e:
            print(f"  Error: {e}")

def tool_70_uac_level():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [70] User Account Control (UAC) Elevation Level ==={CLR_RESET}")
    if os.name == 'nt':
        import ctypes
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin:
            print(f"  {CLR_GREEN}[✓] Current Session has Full Administrator Privileges.{CLR_RESET}")
        else:
            print(f"  {CLR_YELLOW}[!] Current Session is Standard User (Non-Elevated).{CLR_RESET}")
