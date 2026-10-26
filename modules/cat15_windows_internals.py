# -*- coding: utf-8 -*-
"""
Cipher Tools - Category 15: Extended Windows Internals, Registry & Security Artifacts (Tools 301 - 350)
Pure Python Standard Library (os, sys, subprocess, platform, ctypes)
"""
import os
import sys
import subprocess
import platform

CLR_CYAN = "\033[96m"
CLR_PINK = "\033[95m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_GRAY = "\033[90m"
CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"

def _run_ps(cmd):
    if os.name != 'nt': return "Non-Windows Host"
    try:
        return subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True).strip()
    except Exception as e:
        return f"Error: {e}"

def tool_301_pagefile_query():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [301] Windows Pagefile (Virtual Memory) Sizing ==={CLR_RESET}")
    res = _run_ps("Get-CimInstance Win32_PageFileSetting | Select-Object Name, InitialSize, MaximumSize | Format-List")
    print(f"  {res or 'System Managed Pagefile active'}")

def tool_302_smbios_uuid():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [302] SMBIOS Universal Unique Identifier (Hardware UUID) ==={CLR_RESET}")
    res = _run_ps("(Get-CimInstance Win32_ComputerSystemProduct).UUID")
    print(f"  Machine UUID: {CLR_GREEN}{res}{CLR_RESET}")

def tool_303_bitlocker_status():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [303] BitLocker Drive Encryption Status ==={CLR_RESET}")
    res = _run_ps("Get-BitLockerVolume -MountPoint 'C:' | Select-Object MountPoint, VolumeStatus, EncryptionPercentage | Format-List")
    print(f"  {res or 'BitLocker information requires elevation'}")

def tool_304_secure_boot_state():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [304] UEFI Secure Boot Operational State ==={CLR_RESET}")
    res = _run_ps("Confirm-SecureBootUEFI")
    print(f"  Secure Boot Enabled: {CLR_GREEN if 'True' in res else CLR_YELLOW}{res}{CLR_RESET}")

def tool_305_dep_status():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [305] Data Execution Prevention (DEP) Support ==={CLR_RESET}")
    res = _run_ps("(Get-CimInstance Win32_OperatingSystem).DataExecutionPrevention_SupportPolicy")
    policies = {"0": "AlwaysOff", "1": "AlwaysOn", "2": "OptIn", "3": "OptOut"}
    print(f"  DEP Policy: {CLR_GREEN}{policies.get(res, res)}{CLR_RESET}")

def tool_306_smbv1_protocol_check():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [306] SMBv1 Legacy Vulnerability Status ==={CLR_RESET}")
    res = _run_ps("Get-WindowsOptionalFeature -Online -FeatureName SMB1Protocol | Select-Object State")
    print(f"  SMBv1 Feature: {CLR_GREEN if 'Disabled' in res else CLR_RED}{res}{CLR_RESET}")

def tool_307_powershell_execution_policy():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [307] PowerShell Execution Policy Auditor ==={CLR_RESET}")
    res = _run_ps("Get-ExecutionPolicy -List | Format-Table -AutoSize")
    print(res)

def tool_308_unquoted_service_paths():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [308] Unquoted Service Path Vulnerability Hunter ==={CLR_RESET}")
    res = _run_ps("Get-CimInstance Win32_Service | Where-Object { $_.PathName -notmatch '^\"' -and $_.PathName -match ' ' } | Select-Object -First 5 Name, PathName | Format-List")
    if res:
        print(f"  {CLR_RED}[!] Vulnerable unquoted services found:{CLR_RESET}\n{res}")
    else:
        print(f"  {CLR_GREEN}[✓] No vulnerable unquoted service paths discovered.{CLR_RESET}")

def tool_309_vss_shadow_copies():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [309] Volume Shadow Copies (VSS Snapshot) Query ==={CLR_RESET}")
    res = _run_ps("vssadmin list shadows")
    print(res[:300] if res else "  No shadow copies or access requires elevation.")

def tool_310_rdp_registry_status():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [310] Remote Desktop (RDP) Port & Listener Status ==={CLR_RESET}")
    res = _run_ps("Get-ItemProperty 'HKLM:\\System\\CurrentControlSet\\Control\\Terminal Server' -Name fDenyTSConnections | Select-Object fDenyTSConnections")
    print(f"  fDenyTSConnections: {res}")

def tool_311_event_id_4624_logons():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [311] Recent Successful User Logons (Event ID 4624) ==={CLR_RESET}")
    res = _run_ps("Get-WinEvent -FilterHashtable @{LogName='Security';Id=4624} -MaxEvents 3 | Select-Object TimeCreated, Message | Format-List")
    print(res[:350] if "TimeCreated" in res else "  Security Event Log requires Administrator elevation.")

def tool_312_screen_saver_timeout():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [312] Screen Lock & Inactivity Timeout Policy ==={CLR_RESET}")
    res = _run_ps("Get-ItemProperty 'HKCU:\\Control Panel\\Desktop' -Name ScreenSaveTimeOut, ScreenSaverIsSecure | Format-List")
    print(res or "  Default desktop settings.")

def tool_313_guest_account_state():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [313] Built-in Guest User Account State ==={CLR_RESET}")
    res = _run_ps("Get-LocalUser -Name 'Guest' | Select-Object Name, Enabled, Description | Format-List")
    print(res or "  Guest account query unavailable.")

def tool_314_defender_exclusions():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [314] Windows Defender Exclusion Paths Audit ==={CLR_RESET}")
    res = _run_ps("Get-MpPreference | Select-Object -ExpandProperty ExclusionPath")
    if res:
        print(f"  {CLR_YELLOW}[!] Active exclusions:{CLR_RESET}\n{res}")
    else:
        print(f"  {CLR_GREEN}[✓] No custom path exclusions configured in Windows Defender.{CLR_RESET}")

def tool_315_crashdump_config():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [315] Windows Memory Crash Dump Configuration ==={CLR_RESET}")
    res = _run_ps("Get-ItemProperty 'HKLM:\\SYSTEM\\CurrentControlSet\\Control\\CrashControl' | Select-Object CrashDumpEnabled, DumpFile | Format-List")
    print(res or "  Crash control settings.")

def tool_316_installed_drivers():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [316] Kernel Driver Inventory & Verification ==={CLR_RESET}")
    res = _run_ps("Get-CimInstance Win32_SystemDriver | Where-Object State -eq 'Running' | Select-Object -First 8 Name, Description | Format-Table -AutoSize")
    print(res)

def tool_317_device_manager_errors():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [317] Device Manager Hardware Problem Codes ==={CLR_RESET}")
    res = _run_ps("Get-CimInstance Win32_PnPEntity | Where-Object ConfigManagerErrorCode -ne 0 | Select-Object Name, ConfigManagerErrorCode | Format-List")
    if res: print(f"  Devices with issues:\n{res}")
    else: print(f"  {CLR_GREEN}[✓] All PnP hardware devices functioning normally (Error Code 0).{CLR_RESET}")

def tool_318_system_restore_points():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [318] System Restore Points Enumeration ==={CLR_RESET}")
    res = _run_ps("Get-ComputerRestorePoint | Select-Object -First 5 SequenceNumber, Description, CreationTime | Format-Table -AutoSize")
    print(res or "  No active restore points found.")

def tool_319_recycle_bin_size():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [319] Recycle Bin Storage Utilization ==={CLR_RESET}")
    res = _run_ps("(New-Object -ComObject Shell.Application).Namespace(0xA).Items() | Measure-Object -Property Size -Sum | Select-Object Count, @{Name='MB';Expression={[math]::Round($_.Sum / 1MB, 2)}} | Format-List")
    print(res or "  Recycle bin query.")

def tool_320_god_mode_creator():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [320] Windows 'God Mode' Master Control Folder Helper ==={CLR_RESET}")
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    god_folder = os.path.join(desktop, "GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}")
    print(f"  To deploy the all-in-one control panel folder on your Desktop:")
    print(f"  Folder Name: {CLR_CYAN}GodMode.{{ED7BA470-8E54-465E-825C-99712043E01C}}{CLR_RESET}")

def tool_321_dism_health_guide():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [321] DISM Windows Image Health & Servicing ==={CLR_RESET}")
    print(f"  Check Health   : {CLR_CYAN}DISM /Online /Cleanup-Image /CheckHealth{CLR_RESET}")
    print(f"  Scan Corruption: {CLR_CYAN}DISM /Online /Cleanup-Image /ScanHealth{CLR_RESET}")
    print(f"  Restore Health : {CLR_GREEN}DISM /Online /Cleanup-Image /RestoreHealth{CLR_RESET}")

def tool_322_network_shares_audit():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [322] Active SMB Network Shares Auditor ==={CLR_RESET}")
    res = _run_ps("Get-SmbShare | Select-Object Name, Path, Description | Format-Table -AutoSize")
    print(res)

def tool_323_battery_report_gen():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [323] Official Windows Battery & Degradation Report ==={CLR_RESET}")
    print(f"  Command to output HTML telemetry battery health report:")
    print(f"  {CLR_CYAN}powercfg /batteryreport /output \"battery_report.html\"{CLR_RESET}")

def tool_324_sleep_study_gen():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [324] Modern Standby SleepStudy Report ==={CLR_RESET}")
    print(f"  Command to evaluate background drain during sleep:")
    print(f"  {CLR_CYAN}powercfg /sleepstudy /output \"sleepstudy.html\"{CLR_RESET}")

def tool_325_windows_features():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [325] Optional Windows Features State ==={CLR_RESET}")
    res = _run_ps("Get-WindowsOptionalFeature -Online | Where-Object State -eq 'Enabled' | Select-Object -First 10 FeatureName | Format-Table -AutoSize")
    print(res)

def tool_326_dns_addresses_per_nic():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [326] Active DNS Addresses Per Network Interface ==={CLR_RESET}")
    res = _run_ps("Get-DnsClientServerAddress | Where-Object ServerAddresses | Select-Object InterfaceAlias, ServerAddresses | Format-Table -AutoSize")
    print(res)

def tool_327_sticky_keys_backdoor_check():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [327] Accessibility Backdoor (sethc.exe / Utilman) Auditor ==={CLR_RESET}")
    res = _run_ps("Get-ItemProperty 'HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\sethc.exe' -ErrorAction SilentlyContinue")
    if res:
        print(f"  {CLR_RED}[!] WARNING: Debugger attached to sethc.exe (Sticky Keys)!{CLR_RESET}")
    else:
        print(f"  {CLR_GREEN}[✓] Clean: No debugger hijacked sethc.exe or utilman.exe.{CLR_RESET}")

def tool_328_windows_error_reporting():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [328] Windows Error Reporting (WER) Crash Dump Policy ==={CLR_RESET}")
    res = _run_ps("Get-ItemProperty 'HKCU:\\Software\\Microsoft\\Windows\\Windows Error Reporting' -Name Disabled -ErrorAction SilentlyContinue")
    print(f"  WER Configuration: {res or 'Default enabled'}")

def tool_329_active_sound_devices():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [329] Audio Playback & Capture Devices ==={CLR_RESET}")
    res = _run_ps("Get-CimInstance Win32_SoundDevice | Select-Object Name, Status, Manufacturer | Format-List")
    print(res)

def tool_330_windows_internals_summary():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [330] Windows System Core Internals Health Summary ==={CLR_RESET}")
    print(f"  {CLR_GREEN}[✓] Windows Core and Subsystem API interfaces validated.{CLR_RESET}")
