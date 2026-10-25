# -*- coding: utf-8 -*-
"""
Cipher Tools - Category 1: System, OS & Kernel (Tools 1 - 10)
"""
import os
import sys
import time
import platform
import subprocess
from datetime import datetime

CLR_CYAN = "\033[96m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_GRAY = "\033[90m"
CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"

def tool_1_os_arch():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [1] OS Architecture & Kernel Build Info ==={CLR_RESET}")
    uname = platform.uname()
    print(f"  {CLR_GREEN}● Operating System:{CLR_RESET}   {uname.system} {uname.release}")
    print(f"  {CLR_GREEN}● Kernel Build    :{CLR_RESET}   {uname.version}")
    print(f"  {CLR_GREEN}● Machine Arch    :{CLR_RESET}   {uname.machine}")
    print(f"  {CLR_GREEN}● Processor Specs :{CLR_RESET}   {uname.processor or 'x86_64 Compatible'}")
    print(f"  {CLR_GREEN}● Node Name       :{CLR_RESET}   {uname.node}")
    print(f"  {CLR_GREEN}● Python Runtime  :{CLR_RESET}   {platform.python_version()} ({platform.python_compiler()})")

def tool_2_uptime():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [2] Windows Uptime & Boot Time Tracker ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            cmd = "(Get-CimInstance Win32_OperatingSystem).LastBootUpTime"
            out = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True).strip()
            print(f"  {CLR_GREEN}● System Boot Timestamp:{CLR_RESET} {out}")
        except Exception as e:
            print(f"  {CLR_RED}[-] Could not query boot time: {e}{CLR_RESET}")
    else:
        print("  Available on Windows systems.")

def tool_3_hotfixes():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [3] Installed Hotfixes & OS Updates ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            cmd = "Get-HotFix | Select-Object -First 10 HotFixID, InstalledOn, Description | Format-Table -AutoSize"
            out = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True)
            print(out)
        except Exception as e:
            print(f"  {CLR_RED}[-] Query error: {e}{CLR_RESET}")
    else:
        print("  Available on Windows.")

def tool_4_env_vars():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [4] Environment Variables Explorer ==={CLR_RESET}")
    keys = sorted(os.environ.keys())
    print(f"  {CLR_CYAN}Total Active Variables: {len(keys)}{CLR_RESET}\n")
    for k in keys[:15]:
        v = os.environ[k]
        if len(v) > 60: v = v[:57] + "..."
        print(f"  {CLR_GREEN}{k:<24}:{CLR_RESET} {v}")
    if len(keys) > 15:
        print(f"  {CLR_GRAY}... plus {len(keys) - 15} more variables.{CLR_RESET}")

def tool_5_path_validator():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [5] System PATH Validator & Missing Path Detector ==={CLR_RESET}")
    raw_path = os.environ.get("PATH", "")
    paths = raw_path.split(os.pathsep)
    valid_count, missing_count = 0, 0
    for idx, p in enumerate(paths, 1):
        if os.path.isdir(p):
            valid_count += 1
            print(f"  {idx:<2}. {CLR_GREEN}[VALID]{CLR_RESET}   {p}")
        else:
            missing_count += 1
            print(f"  {idx:<2}. {CLR_RED}[MISSING]{CLR_RESET} {p}")
    print(f"\n  Summary: {CLR_GREEN}{valid_count} Valid{CLR_RESET} | {CLR_RED}{missing_count} Broken/Missing{CLR_RESET}")

def tool_6_power_scheme():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [6] Windows Power Scheme & Battery Status ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            res = subprocess.check_output(["powercfg", "/getactivescheme"], text=True)
            print(f"  {CLR_CYAN}Active Scheme:{CLR_RESET} {res.strip()}")
            batt_cmd = "Get-CimInstance Win32_Battery | Select-Object EstimatedChargeRemaining, BatteryStatus | Format-List"
            batt_res = subprocess.check_output(["powershell", "-NoProfile", "-Command", batt_cmd], text=True).strip()
            if batt_res:
                print(f"  {batt_res}")
            else:
                print(f"  {CLR_GRAY}Battery: Desktop system (AC power line){CLR_RESET}")
        except Exception as e:
            print(f"  {CLR_RED}[-] Power check failed: {e}{CLR_RESET}")
    else:
        print("  Windows PowerCfg tool.")

def tool_7_active_sessions():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [7] Active Logged-in Sessions & Users ==={CLR_RESET}")
    print(f"  {CLR_GREEN}Current Operator User:{CLR_RESET} {os.getenv('USERNAME') or 'TheCIpher'}")
    if os.name == 'nt':
        try:
            out = subprocess.check_output(["query", "user"], text=True)
            print(f"\n{out}")
        except Exception:
            print(f"  User Domain: {os.getenv('USERDOMAIN', 'WORKGROUP')}")

def tool_8_bios_motherboard():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [8] BIOS / Motherboard Manufacturer & Serial ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            cmd = "Get-CimInstance Win32_BaseBoard | Select-Object Manufacturer, Product, SerialNumber | Format-List"
            out = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True)
            print(out.strip())
        except Exception as e:
            print(f"  {CLR_RED}[-] Error: {e}{CLR_RESET}")
    else:
        print("  Windows BaseBoard CIM query.")

def tool_9_locale_timezone():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [9] System Locale, Codepage & Timezone ==={CLR_RESET}")
    print(f"  {CLR_GREEN}● Local Timestamp:{CLR_RESET}   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  {CLR_GREEN}● UTC Timestamp  :{CLR_RESET}   {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  {CLR_GREEN}● Default Encoding:{CLR_RESET}  {sys.getdefaultencoding()}")
    print(f"  {CLR_GREEN}● Filesystem Code:{CLR_RESET}   {sys.getfilesystemencoding()}")
    if hasattr(time, 'tzname'):
        print(f"  {CLR_GREEN}● Timezone Name  :{CLR_RESET}   {time.tzname[0]}")

def tool_10_shutdown_timer():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [10] Windows Shutdown / Reboot Timer ==={CLR_RESET}")
    print("  [1] Abort any existing shutdown timer")
    print("  [2] Schedule shutdown in N minutes")
    print("  [3] Schedule restart in N minutes")
    choice = input(f"  {CLR_YELLOW}Select Option [1-3]:{CLR_RESET} ").strip()
    if choice == '1':
        os.system("shutdown /a")
        print(f"  {CLR_GREEN}[✓] Shutdown schedule aborted.{CLR_RESET}")
    elif choice in ('2', '3'):
        try:
            mins = int(input("  Enter minutes: ") or "10")
            secs = mins * 60
            flag = "/s" if choice == '2' else "/r"
            os.system(f"shutdown {flag} /t {secs}")
            print(f"  {CLR_GREEN}[✓] Operation scheduled in {mins} minutes ({secs} seconds).{CLR_RESET}")
        except Exception as e:
            print(f"  {CLR_RED}[-] Error: {e}{CLR_RESET}")
