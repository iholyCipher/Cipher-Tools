# -*- coding: utf-8 -*-
"""
Cipher Tools - Category 8: Binary Forensics & Reverse Engineering (Tools 71 - 80)
"""
import os
import sys
import re
import math
import mimetypes
import struct
import hashlib

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
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [74] Deep Windows PE Binary Architecture & Section Analyzer ==={CLR_RESET}")
    p = input('  Enter PE executable file (.exe/.dll/.sys): ').strip(' "\'') or sys.executable
    if not os.path.isfile(p):
        print(f"  {CLR_RED}[-] File not found: {p}{CLR_RESET}")
        return
    with open(p, 'rb') as f:
        data = f.read()
    if len(data) < 64 or data[:2] != b"MZ":
        print(f"  {CLR_RED}[-] Not a valid DOS/MZ executable binary.{CLR_RESET}")
        return
    e_lfanew = struct.unpack_from("<I", data, 0x3C)[0]
    if e_lfanew + 24 > len(data) or data[e_lfanew:e_lfanew+4] != b"PE\x00\x00":
        print(f"  {CLR_RED}[-] Missing NT PE\0\0 signature at offset 0x{e_lfanew:X}.{CLR_RESET}")
        return
    coff = e_lfanew + 4
    machine, num_sections, timedate, sym_ptr, num_syms, opt_size, chars = struct.unpack_from("<HHIIIHH", data, coff)
    opt_offset = coff + 20
    magic = struct.unpack_from("<H", data, opt_offset)[0]
    is_64 = (magic == 0x20B)
    arch = "PE32+ (x64 Architecture)" if is_64 else "PE32 (x86 32-bit)"
    
    if is_64:
        entry_point, image_base = struct.unpack_from("<IQ", data, opt_offset + 16)
        subsystem = struct.unpack_from("<H", data, opt_offset + 68)[0]
    else:
        entry_point, image_base = struct.unpack_from("<II", data, opt_offset + 16)
        subsystem = struct.unpack_from("<H", data, opt_offset + 68)[0]
        
    subsystem_names = {1: "Native Driver", 2: "Windows GUI", 3: "Windows CUI (Console)", 7: "POSIX", 9: "Windows CE", 10: "EFI Application"}
    sub_desc = subsystem_names.get(subsystem, f"Subsystem {subsystem}")
    
    print(f"  Format Architecture: {CLR_CYAN}{arch}{CLR_RESET}")
    print(f"  Entry Point (RVA)  : 0x{entry_point:08X} | Image Base: 0x{image_base:X}")
    print(f"  Subsystem Type     : {sub_desc} | Sections Count: {num_sections}")
    print(f"\n  {CLR_BOLD}PE Section Table & Permissions Breakdown:{CLR_RESET}")
    print(f"  {'-'*65}")
    print(f"  {'Section':<10} {'VirtAddr':<12} {'RawSize':<10} {'RawOffset':<12} {'Flags'}")
    print(f"  {'-'*65}")
    
    sec_offset = opt_offset + opt_size
    for _ in range(num_sections):
        if sec_offset + 40 > len(data): break
        s_data = data[sec_offset:sec_offset+40]
        name = s_data[:8].rstrip(b"\x00").decode("ascii", errors="ignore")
        v_size, v_addr, r_size, r_offset = struct.unpack_from("<IIII", s_data, 8)
        c_flags = struct.unpack_from("<I", s_data, 36)[0]
        perms = ("R" if (c_flags & 0x40000000) else "-") + \
                ("W" if (c_flags & 0x80000000) else "-") + \
                ("X" if (c_flags & 0x20000000) else "-")
        print(f"  {name:<10} 0x{v_addr:08X}   {r_size:<10} 0x{r_offset:08X}   [{perms}]")
        sec_offset += 40
    print(f"  {CLR_GREEN}[✓] PE binary structural analysis completed successfully.{CLR_RESET}")

def tool_75_file_entropy():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [75] Sliding-Window Shannon Entropy Scanner & Density Map ==={CLR_RESET}")
    p = input('  Enter binary file to scan: ').strip(' "\'') or sys.executable
    if not os.path.isfile(p):
        print(f"  {CLR_RED}[-] File not found: {p}{CLR_RESET}")
        return
    with open(p, 'rb') as f:
        data = f.read(2 * 1024 * 1024)
    if not data:
        print("  File is empty.")
        return
        
    l = len(data)
    freq = {}
    for b in data: freq[b] = freq.get(b, 0) + 1
    total_entropy = -sum((c/l) * math.log2(c/l) for c in freq.values())
    
    print(f"  Total Binary Size  : {l:,} bytes")
    print(f"  Mean Shannon Metric: {CLR_CYAN}{total_entropy:.4f} / 8.000 bits{CLR_RESET}")
    
    window = 512
    step = 256
    slices = []
    offset = 0
    while offset < l:
        chunk = data[offset : offset + window]
        if not chunk: break
        cl = len(chunk)
        cfreq = {}
        for b in chunk: cfreq[b] = cfreq.get(b, 0) + 1
        cent = -sum((c/cl) * math.log2(c/cl) for c in cfreq.values())
        slices.append((offset, cent))
        offset += step
        
    print(f"\n  {CLR_BOLD}Sliding Density Profile (sampled 16 blocks across binary):{CLR_RESET}")
    print(f"  {'-'*65}")
    stride = max(1, len(slices) // 16)
    for off, ent in slices[::stride][:16]:
        bar_len = int((ent / 8.0) * 16)
        bar = "=" * bar_len + "." * (16 - bar_len)
        if ent >= 7.2:
            st = f"{CLR_RED}PACKED / ENCRYPTED{CLR_RESET}"
        elif ent >= 5.5:
            st = f"{CLR_YELLOW}EXECUTABLE CODE{CLR_RESET}"
        elif ent >= 3.0:
            st = f"{CLR_CYAN}STRUCTURED DATA{CLR_RESET}"
        else:
            st = f"{CLR_GRAY}SPARSE / ZERO-PADDED{CLR_RESET}"
        print(f"  Offset 0x{off:06X} [{bar}] {ent:4.2f} bits | {st}")
    print(f"  {'-'*65}")
    print(f"  {CLR_GREEN}[✓] Sliding-window entropy profiling completed successfully.{CLR_RESET}")

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
