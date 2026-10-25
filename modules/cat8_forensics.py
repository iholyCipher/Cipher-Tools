# -*- coding: utf-8 -*-
"""
Cipher Tools - Category 8: Binary Forensics & Reverse Engineering (Tools 71 - 80)
"""
import os
import sys
import re
import math
import mimetypes

CLR_CYAN = "\033[96m"
CLR_PINK = "\033[95m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_GRAY = "\033[90m"
CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"

def tool_71_hex_viewer():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [71] Binary Hex Viewer ==={CLR_RESET}")
    p = input("  Enter file path: ").strip(' "\'')
    if not os.path.isfile(p): return
    with open(p, 'rb') as f: chunk = f.read(128)
    for i in range(0, len(chunk), 16):
        b = chunk[i:i+16]
        hx = " ".join(f"{x:02X}" for x in b)
        asc = "".join(chr(x) if 32 <= x <= 126 else "." for x in b)
        print(f"  {i:04X}  {hx:<48}  |{asc}|")

def tool_72_magic_bytes():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [72] Magic Bytes File Signature Identifier ==={CLR_RESET}")
    p = input("  Enter file path: ").strip(' "\'')
    if not os.path.isfile(p): return
    with open(p, 'rb') as f: head = f.read(32)
    sigs = {
        b"MZ": "Windows PE Executable / DLL",
        b"\x7fELF": "Linux ELF Executable",
        b"%PDF": "Adobe PDF Document",
        b"PK\x03\x04": "ZIP / DOCX / APK Archive",
        b"\xff\xd8\xff": "JPEG Graphic Image",
        b"\x89PNG": "PNG Graphic Image",
        b"Rar!\x1a\x07": "RAR Archive",
        b"7z\xbc\xaf\x27\x1c": "7-Zip Archive"
    }
    match = "Unknown Stream"
    for s, desc in sigs.items():
        if head.startswith(s): match = desc; break
    print(f"  {CLR_GREEN}Signature:{CLR_RESET} {match}")

def tool_73_string_extract():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [73] ASCII & Unicode String Extractor ==={CLR_RESET}")
    p = input("  Enter binary file: ").strip(' "\'')
    if not os.path.isfile(p): return
    with open(p, 'rb') as f: data = f.read(512 * 1024)
    matches = re.findall(rb'[A-Za-z0-9/\-:._]{5,}', data)
    for m in matches[:15]:
        print(f"  ➜ {m.decode('latin1', errors='ignore')}")

def tool_74_pe_header():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [74] Windows PE Executable Analyzer ==={CLR_RESET}")
    p = input("  Enter .exe file: ").strip(' "\'')
    if not os.path.isfile(p): return
    with open(p, 'rb') as f:
        dos = f.read(64)
        if not dos.startswith(b"MZ"):
            print("  Not a Windows PE file.")
            return
        e_lfanew = int.from_bytes(dos[60:64], 'little')
        f.seek(e_lfanew)
        pe_sig = f.read(4)
        if pe_sig == b"PE\x00\x00":
            print(f"  {CLR_GREEN}[✓] Valid PE Header verified at offset 0x{e_lfanew:X}{CLR_RESET}")

def tool_75_file_entropy():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [75] File Entropy Calculator (Packed / Encrypted Binary Detector) ==={CLR_RESET}")
    p = input("  Enter file: ").strip(' "\'')
    if not os.path.isfile(p): return
    with open(p, 'rb') as f: data = f.read(1024 * 1024)
    if not data: return
    entropy = 0
    for x in range(256):
        p_x = float(data.count(x)) / len(data)
        if p_x > 0: entropy += - p_x * math.log2(p_x)
    print(f"  Entropy: {CLR_CYAN}{entropy:.3f} / 8.000 bits{CLR_RESET}")
    if entropy > 7.2: print(f"  Status: {CLR_RED}Likely Encrypted, Compressed or Packed{CLR_RESET}")
    elif entropy > 5.5: print(f"  Status: {CLR_YELLOW}Normal Code / Executable{CLR_RESET}")
    else: print(f"  Status: {CLR_GREEN}Plaintext / Uncompressed Data{CLR_RESET}")

def tool_76_binary_diff():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [76] Binary Difference Comparator ==={CLR_RESET}")
    f1 = input("  Enter file 1: ").strip(' "\'')
    f2 = input("  Enter file 2: ").strip(' "\'')
    if not (os.path.isfile(f1) and os.path.isfile(f2)): return
    with open(f1, 'rb') as a, open(f2, 'rb') as b:
        d1, d2 = a.read(1024), b.read(1024)
        diffs = sum(1 for x, y in zip(d1, d2) if x != y)
        print(f"  Byte differences in first 1KB: {CLR_YELLOW}{diffs}{CLR_RESET}")

def tool_77_base64_in_binary():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [77] Base64 Extractor from Binary Data ==={CLR_RESET}")
    p = input("  Enter binary file: ").strip(' "\'')
    if not os.path.isfile(p): return
    with open(p, 'rb') as f: data = f.read(512 * 1024)
    b64_matches = re.findall(rb'(?:[A-Za-z0-9+/]{4}){8,}(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?', data)
    print(f"  Discovered {len(b64_matches)} possible Base64 blocks:")
    for b in b64_matches[:5]:
        print(f"  ➜ {b.decode('latin1', errors='ignore')[:60]}...")

def tool_78_ip_regex_scanner():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [78] IP & URL Regex Finder in Files ==={CLR_RESET}")
    p = input("  Enter file to search: ").strip(' "\'')
    if not os.path.isfile(p): return
    with open(p, 'rb') as f: data = f.read(1024 * 1024)
    ips = re.findall(rb'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', data)
    urls = re.findall(rb'https?://[A-Za-z0-9./\-_]+', data)
    print(f"  IP Addresses ({len(ips)}): {[x.decode() for x in set(ips[:10])]}")
    print(f"  URLs ({len(urls)}): {[x.decode() for x in set(urls[:5])]}")

def tool_79_timestomp_check():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [79] File Timestamp Integrity Check ==={CLR_RESET}")
    p = input("  Enter file: ").strip(' "\'')
    if not os.path.isfile(p): return
    st = os.stat(p)
    from datetime import datetime
    print(f"  Created : {datetime.fromtimestamp(st.st_ctime)}")
    print(f"  Modified: {datetime.fromtimestamp(st.st_mtime)}")
    print(f"  Accessed: {datetime.fromtimestamp(st.st_atime)}")

def tool_80_mime_guess():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [80] File MIME Type Guessing Engine ==={CLR_RESET}")
    p = input("  Enter filename or path: ").strip(' "\'')
    mtype, _ = mimetypes.guess_type(p)
    print(f"  Guessed MIME: {CLR_GREEN}{mtype or 'application/octet-stream'}{CLR_RESET}")
