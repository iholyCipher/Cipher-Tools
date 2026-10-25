# -*- coding: utf-8 -*-
"""
Cipher Tools - Category 9: Windows Administration & Registry (Tools 81 - 90)
"""
import os
import sys
import subprocess

CLR_CYAN = "\033[96m"
CLR_PINK = "\033[95m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_GRAY = "\033[90m"
CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"

def tool_81_startup_items():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [81] Windows Startup & Persistence ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            cmd = "Get-CimInstance Win32_StartupCommand | Select-Object -First 10 Name, Command, User | Format-Table -AutoSize"
            out = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True)
            print(out)
        except Exception as e: print(f"  Error: {e}")

def tool_82_services_status():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [82] Windows Services Inspector ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            cmd = "Get-Service | Where-Object Status -eq 'Running' | Select-Object -First 12 Name, DisplayName | Format-Table -AutoSize"
            out = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True)
            print(out)
        except Exception as e: print(f"  Error: {e}")

def tool_83_event_errors():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [83] Windows Event Log Critical Errors ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            cmd = "Get-EventLog -LogName System -EntryType Error -Newest 5 | Select-Object TimeGenerated, Source, Message | Format-List"
            out = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True)
            print(out.strip())
        except Exception as e: print(f"  Notice: {e}")

def tool_84_installed_apps():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [84] Installed Programs Inventory ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            cmd = "Get-ItemProperty HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Where-Object DisplayName | Select-Object -First 12 DisplayName, DisplayVersion | Format-Table -AutoSize"
            out = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True)
            print(out)
        except Exception as e: print(f"  Error: {e}")

def tool_85_defender_status():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [85] Windows Defender Status ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            cmd = "Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, AntivirusSignatureAge | Format-List"
            out = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True)
            print(out.strip())
        except Exception as e: print(f"  Query error: {e}")

def tool_86_flush_dns():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [86] DNS Resolver Cache Purger ==={CLR_RESET}")
    if os.name == 'nt':
        res = subprocess.run(["ipconfig", "/flushdns"], stdout=subprocess.PIPE, text=True)
        print(f"  {CLR_GREEN}[✓] {res.stdout.strip()}{CLR_RESET}")

def tool_87_task_scheduler():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [87] Task Scheduler Active Jobs ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            cmd = "Get-ScheduledTask | Where-Object State -eq 'Ready' | Select-Object -First 10 TaskName, TaskPath | Format-Table -AutoSize"
            out = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True)
            print(out)
        except Exception as e: print(f"  Error: {e}")

def tool_88_product_key():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [88] Windows Digital License Query ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            cmd = "(Get-CimInstance SoftwareLicensingProduct | Where-Object PartialProductKey | Select-Object -First 1).Name"
            out = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True)
            print(f"  License: {out.strip()}")
        except Exception as e: print(f"  Query error: {e}")

def tool_89_sfc_helper():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [89] System File Checker (SFC) Guide ==={CLR_RESET}")
    print("  To repair Windows system files, launch Administrator CMD and run:")
    print(f"  {CLR_CYAN}sfc /scannow{CLR_RESET}")
    print("  Or deployment servicing tool:")
    print(f"  {CLR_CYAN}DISM /Online /Cleanup-Image /RestoreHealth{CLR_RESET}")

def tool_90_windows_update():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [90] Windows Update Service State ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            cmd = "Get-Service wuauserv | Select-Object Status, StartType | Format-List"
            out = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True)
            print(out.strip())
        except Exception as e: print(f"  Error: {e}")
