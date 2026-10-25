# -*- coding: utf-8 -*-
"""
Cipher Tools - Category 3: Storage, Disk & File System Forensics (Tools 21 - 30)
"""
import os
import sys
import hashlib
import shutil
import zipfile
import subprocess

CLR_CYAN = "\033[96m"
CLR_PINK = "\033[95m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_GRAY = "\033[90m"
CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"

def tool_21_partition_graph():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [21] Partition Capacity & Percentage Bar Graph ==={CLR_RESET}")
    if os.name == 'nt':
        import ctypes
        for drive in ["C:\\", "D:\\", "E:\\", "F:\\", "G:\\"]:
            if os.path.exists(drive):
                try:
                    free_b = ctypes.c_ulonglong(0)
                    total_b = ctypes.c_ulonglong(0)
                    ctypes.windll.kernel32.GetDiskFreeSpaceExW(drive, ctypes.byref(free_b), ctypes.byref(total_b), None)
                    t_gb = total_b.value / (1024**3)
                    f_gb = free_b.value / (1024**3)
                    u_gb = t_gb - f_gb
                    pct = (u_gb / t_gb) * 100 if t_gb > 0 else 0
                    bar_len = 20
                    filled = int(bar_len * (pct / 100))
                    bar = f"{CLR_PINK}{'█' * filled}{CLR_GRAY}{'░' * (bar_len - filled)}{CLR_RESET}"
                    print(f"  Drive {drive:<3} [{bar}] {pct:5.1f}% ({u_gb:.1f}/{t_gb:.1f} GB)")
                except Exception:
                    pass

def tool_22_duplicate_finder():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [22] SHA-256 Duplicate File Finder ==={CLR_RESET}")
    path = input("  Enter directory to scan: ").strip(' "\'')
    if not os.path.isdir(path):
        print(f"  {CLR_RED}[-] Invalid directory.{CLR_RESET}")
        return
    print(f"  {CLR_CYAN}[*] Scanning files...{CLR_RESET}")
    hashes, dups = {}, []
    for root, _, files in os.walk(path):
        for f in files:
            full = os.path.join(root, f)
            try:
                if os.path.getsize(full) == 0: continue
                h = hashlib.sha256()
                with open(full, 'rb') as fp:
                    while chk := fp.read(131072): h.update(chk)
                dg = h.hexdigest()
                if dg in hashes: dups.append((hashes[dg], full))
                else: hashes[dg] = full
            except Exception: pass
    print(f"  {CLR_GREEN}[✓] Found {len(dups)} duplicate pairs.{CLR_RESET}")
    for orig, dup in dups[:10]:
        print(f"  Master: {orig}\n  Clone : {dup}\n")

def tool_23_folder_tree():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [23] Recursive Directory Space Consumption Tree ==={CLR_RESET}")
    path = input("  Enter directory path: ").strip(' "\'')
    if not os.path.isdir(path): return
    items = []
    for entry in os.scandir(path):
        sz = 0
        if entry.is_dir():
            for r, _, fs in os.walk(entry.path):
                for f in fs:
                    try: sz += os.path.getsize(os.path.join(r, f))
                    except Exception: pass
            items.append((entry.name + "/", sz))
        else:
            try: items.append((entry.name, entry.stat().st_size))
            except Exception: pass
    items.sort(key=lambda x: x[1], reverse=True)
    for name, s in items[:12]:
        mb = s / (1024 * 1024)
        print(f"  {name[:35]:<36} {mb:.2f} MB")

def tool_24_empty_pruner():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [24] Ghost Folder Pruner (Empty Directory Eraser) ==={CLR_RESET}")
    target = input("  Enter root path to prune: ").strip(' "\'')
    if not os.path.isdir(target): return
    rm_count = 0
    for root, dirs, _ in os.walk(target, topdown=False):
        for d in dirs:
            dp = os.path.join(root, d)
            try:
                if not os.listdir(dp):
                    os.rmdir(dp)
                    rm_count += 1
            except Exception: pass
    print(f"  {CLR_GREEN}[✓] Pruned {rm_count} empty directories.{CLR_RESET}")

def tool_25_archive_extractor():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [25] Smart Archive Search, Auto-Extract & Explorer Launch ==={CLR_RESET}")
    q = input("  Enter archive name/keyword (e.g. 'mvp', 'backup.zip'): ").strip().lower()
    if not q: return
    user_home = os.path.expanduser("~")
    roots = [os.path.join(user_home, "Downloads"), os.path.join(user_home, "Desktop"), os.path.join(user_home, "Documents")]
    valid_exts = {".zip", ".rar", ".7z", ".tar", ".gz"}
    matches = []
    for r in roots:
        if not os.path.exists(r): continue
        for root, _, files in os.walk(r):
            for f in files:
                ext = os.path.splitext(f.lower())[1]
                if ext in valid_exts and q in f.lower():
                    matches.append(os.path.join(root, f))
    if not matches:
        print(f"  {CLR_RED}[-] No matching archives found.{CLR_RESET}")
        return
    for i, m in enumerate(matches, 1):
        print(f"  [{i}] {m}")
    choice = input(f"  Select archive [1-{len(matches)}]: ").strip()
    idx = int(choice) - 1 if choice.isdigit() and 1 <= int(choice) <= len(matches) else 0
    target = matches[idx]
    dest = os.path.splitext(target)[0] + "_Extracted"
    os.makedirs(dest, exist_ok=True)
    print(f"  {CLR_CYAN}[*] Extracting to {dest}...{CLR_RESET}")
    seven_z = r"C:\Program Files\7-Zip\7z.exe"
    done = False
    if os.path.exists(seven_z):
        subprocess.run([seven_z, "x", "-y", f"-o{dest}", target], stdout=subprocess.DEVNULL)
        done = True
    elif target.lower().endswith(".zip"):
        with zipfile.ZipFile(target, 'r') as zf: zf.extractall(dest)
        done = True
    if done and os.name == 'nt':
        os.startfile(dest)
        print(f"  {CLR_GREEN}[✓] Extracted & opened in Explorer!{CLR_RESET}")

def tool_26_batch_rename():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [26] Batch File Extension Renamer ==={CLR_RESET}")
    folder = input("  Enter folder path: ").strip(' "\'')
    old_ext = input("  Enter old extension (e.g. .jpeg): ").strip()
    new_ext = input("  Enter new extension (e.g. .jpg): ").strip()
    if not os.path.isdir(folder): return
    cnt = 0
    for f in os.listdir(folder):
        if f.endswith(old_ext):
            old_p = os.path.join(folder, f)
            new_p = os.path.join(folder, f[:-len(old_ext)] + new_ext)
            try:
                os.rename(old_p, new_p)
                cnt += 1
            except Exception: pass
    print(f"  {CLR_GREEN}[✓] Renamed {cnt} files.{CLR_RESET}")

def tool_27_create_checksum():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [27] Checksum Manifest Creator (.sha256) ==={CLR_RESET}")
    folder = input("  Enter folder path: ").strip(' "\'')
    if not os.path.isdir(folder): return
    out_file = os.path.join(folder, "manifest.sha256")
    cnt = 0
    with open(out_file, 'w', encoding='utf-8') as out:
        for f in os.listdir(folder):
            full = os.path.join(folder, f)
            if os.path.isfile(full) and f != "manifest.sha256":
                h = hashlib.sha256()
                with open(full, 'rb') as fp:
                    while chk := fp.read(65536): h.update(chk)
                out.write(f"{h.hexdigest()}  {f}\n")
                cnt += 1
    print(f"  {CLR_GREEN}[✓] Manifest generated with {cnt} file hashes at: {out_file}{CLR_RESET}")

def tool_28_verify_checksum():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [28] Checksum Manifest Verifier ==={CLR_RESET}")
    mf = input("  Enter manifest.sha256 path: ").strip(' "\'')
    if not os.path.isfile(mf): return
    folder = os.path.dirname(mf)
    verified, failed = 0, 0
    with open(mf, 'r', encoding='utf-8') as fp:
        for line in fp:
            parts = line.strip().split("  ", 1)
            if len(parts) == 2:
                exp_h, fname = parts
                target = os.path.join(folder, fname)
                if os.path.isfile(target):
                    h = hashlib.sha256()
                    with open(target, 'rb') as tf:
                        while chk := tf.read(65536): h.update(chk)
                    if h.hexdigest().lower() == exp_h.lower():
                        verified += 1
                    else:
                        print(f"  {CLR_RED}[FAIL]{CLR_RESET} {fname}")
                        failed += 1
    print(f"  Summary: {CLR_GREEN}{verified} Verified{CLR_RESET} | {CLR_RED}{failed} Corrupted{CLR_RESET}")

def tool_29_zero_byte_finder():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [29] Zero-Byte / Corrupted File Finder ==={CLR_RESET}")
    path = input("  Enter folder path to check: ").strip(' "\'')
    if not os.path.isdir(path): return
    zero_files = []
    for root, _, files in os.walk(path):
        for f in files:
            full = os.path.join(root, f)
            try:
                if os.path.getsize(full) == 0: zero_files.append(full)
            except Exception: pass
    print(f"  {CLR_CYAN}Found {len(zero_files)} zero-byte files.{CLR_RESET}")
    for z in zero_files[:10]:
        print(f"  {z}")

def tool_30_largest_files():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [30] Largest Files Finder in Target Directory ==={CLR_RESET}")
    path = input("  Enter directory to inspect: ").strip(' "\'')
    if not os.path.isdir(path): return
    all_files = []
    for root, _, files in os.walk(path):
        for f in files:
            full = os.path.join(root, f)
            try: all_files.append((full, os.path.getsize(full)))
            except Exception: pass
    all_files.sort(key=lambda x: x[1], reverse=True)
    print(f"  Top 10 Largest Files:")
    for f, sz in all_files[:10]:
        mb = sz / (1024 * 1024)
        print(f"  {mb:8.2f} MB | {f}")
