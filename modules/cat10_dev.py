# -*- coding: utf-8 -*-
"""
Cipher Tools - Category 10: Productivity, Converters & Developer Utilities (Tools 91 - 100)
"""
import os
import sys
import json
import re
from datetime import datetime

CLR_CYAN = "\033[96m"
CLR_PINK = "\033[95m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_GRAY = "\033[90m"
CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"

def tool_91_unix_epoch():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [91] Unix Epoch Timestamp Converter ==={CLR_RESET}")
    print(f"  Current Epoch: {int(datetime.now().timestamp())}")
    val = input("  Enter Epoch timestamp to convert (or Enter for current): ").strip()
    ts = int(val) if val.isdigit() else int(datetime.now().timestamp())
    dt = datetime.fromtimestamp(ts)
    print(f"  {CLR_GREEN}Formatted Time:{CLR_RESET} {dt.strftime('%Y-%m-%d %H:%M:%S')}")

def tool_92_json_formatter():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [92] JSON Pretty Printer & Syntax Validator ==={CLR_RESET}")
    raw = input("  Enter JSON string: ").strip()
    try:
        obj = json.loads(raw)
        print(json.dumps(obj, indent=2))
        print(f"  {CLR_GREEN}[✓] Valid JSON format.{CLR_RESET}")
    except Exception as e:
        print(f"  {CLR_RED}[-] Invalid JSON: {e}{CLR_RESET}")

def tool_93_xml_formatter():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [93] XML / HTML Tag Stripper ==={CLR_RESET}")
    raw = input("  Enter HTML/XML snippet: ")
    clean = re.sub(r'<[^>]+>', '', raw)
    print(f"  {CLR_GREEN}Stripped Text:{CLR_RESET} {clean}")

def tool_94_cidr_calc():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [94] CIDR Prefix to Subnet Mask Calculator ==={CLR_RESET}")
    p = input("  Enter CIDR prefix (e.g. 24): ").strip()
    if p.isdigit():
        bits = int(p)
        if 0 <= bits <= 32:
            mask = (0xFFFFFFFF << (32 - bits)) & 0xFFFFFFFF
            octets = [(mask >> (8 * i)) & 0xFF for i in reversed(range(4))]
            print(f"  Subnet Mask: {CLR_GREEN}{'.'.join(map(str, octets))}{CLR_RESET}")
            hosts = (2 ** (32 - bits)) - 2 if bits < 31 else 1
            print(f"  Usable Host IPs: {CLR_CYAN}{max(0, hosts):,}{CLR_RESET}")

def tool_95_base_converter():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [95] Number Base Converter ==={CLR_RESET}")
    num_str = input("  Enter integer value: ").strip()
    try:
        n = int(num_str, 0)
        print(f"  Decimal: {n}")
        print(f"  Hex    : {hex(n)}")
        print(f"  Binary : {bin(n)}")
        print(f"  Octal  : {oct(n)}")
    except Exception as e: print(f"  Invalid number: {e}")

def tool_96_word_counter():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [96] Word, Line & Character Counter ==={CLR_RESET}")
    text = input("  Enter paragraph of text: ")
    words = text.split()
    chars = len(text)
    read_sec = len(words) / 3.3
    print(f"  Words     : {len(words)}")
    print(f"  Characters: {chars}")
    print(f"  Read Time : ~{read_sec:.1f} seconds")

def tool_97_case_converter():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [97] Text Case Converter ==={CLR_RESET}")
    t = input("  Enter sentence: ").strip()
    words = re.findall(r'[A-Za-z0-9]+', t)
    if words:
        snake = "_".join(w.lower() for w in words)
        kebab = "-".join(w.lower() for w in words)
        camel = words[0].lower() + "".join(w.capitalize() for w in words[1:])
        pascal = "".join(w.capitalize() for w in words)
        print(f"  snake_case : {snake}")
        print(f"  kebab-case : {kebab}")
        print(f"  camelCase  : {camel}")
        print(f"  PascalCase : {pascal}")

def tool_98_markdown_strip():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [98] Markdown to Plaintext Converter ==={CLR_RESET}")
    md = input("  Enter markdown text: ")
    clean = re.sub(r'[*_#`~>\[\]()]', '', md)
    print(f"  Plaintext: {clean.strip()}")

def tool_99_regex_tester():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [99] Regex Pattern Tester ==={CLR_RESET}")
    pat = input("  Enter regex pattern (e.g. \\d{3}-\\d{4}): ")
    test_str = input("  Enter text to search within: ")
    try:
        m = re.findall(pat, test_str)
        print(f"  {CLR_GREEN}Matches Found ({len(m)}):{CLR_RESET} {m}")
    except Exception as e: print(f"  Regex Error: {e}")

def tool_100_scratch_vault():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [100] Developer Quick Scratchpad ==={CLR_RESET}")
    vault_file = os.path.join(os.path.dirname(__file__), "..", "scratch_notes.txt")
    print("  [1] View Notes")
    print("  [2] Append New Note")
    c = input("  Select: ").strip()
    if c == '1':
        if os.path.exists(vault_file):
            with open(vault_file, 'r', encoding='utf-8') as f:
                print(f.read())
        else: print("  Scratchpad is currently empty.")
    elif c == '2':
        note = input("  Type note: ")
        with open(vault_file, 'a', encoding='utf-8') as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] {note}\n")
        print(f"  {CLR_GREEN}[✓] Note saved to scratchpad!{CLR_RESET}")
