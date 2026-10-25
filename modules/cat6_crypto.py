# -*- coding: utf-8 -*-
"""
Cipher Tools - Category 6: Cryptography, Hashes & Ciphers (Tools 51 - 60)
"""
import os
import sys
import math
import hmac
import uuid
import base64
import string
import secrets
import hashlib

CLR_CYAN = "\033[96m"
CLR_PINK = "\033[95m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_GRAY = "\033[90m"
CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"

def tool_51_multi_hash():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [51] Multi-Hash Calculator (MD5, SHA1, SHA256, SHA512) ==={CLR_RESET}")
    val = input("  Enter string or file path: ").strip(' "\'')
    if os.path.isfile(val):
        with open(val, 'rb') as fp: data = fp.read()
    else: data = val.encode('utf-8')
    print(f"  {CLR_GREEN}MD5   :{CLR_RESET} {hashlib.md5(data).hexdigest()}")
    print(f"  {CLR_GREEN}SHA1  :{CLR_RESET} {hashlib.sha1(data).hexdigest()}")
    print(f"  {CLR_GREEN}SHA256:{CLR_RESET} {hashlib.sha256(data).hexdigest()}")
    print(f"  {CLR_GREEN}SHA512:{CLR_RESET} {hashlib.sha512(data).hexdigest()}")

def tool_52_hash_ident():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [52] Hash Type Algorithmic Identifier ==={CLR_RESET}")
    h = input("  Enter hash string: ").strip()
    l = len(h)
    is_hex = all(c in string.hexdigits for c in h)
    if is_hex:
        if l == 32: print(f"  {CLR_GREEN}Algorithm:{CLR_RESET} MD5 / NTLM")
        elif l == 40: print(f"  {CLR_GREEN}Algorithm:{CLR_RESET} SHA-1")
        elif l == 64: print(f"  {CLR_GREEN}Algorithm:{CLR_RESET} SHA-256")
        elif l == 128: print(f"  {CLR_GREEN}Algorithm:{CLR_RESET} SHA-512")
        else: print(f"  Unknown Hex hash length: {l}")
    else:
        print("  Non-hexadecimal hash.")

def tool_53_xor_cipher():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [53] Symmetric XOR Stream Cipher ==={CLR_RESET}")
    txt = input("  Enter text: ")
    k = input("  Enter secret key: ")
    if k:
        res = "".join(chr(ord(c) ^ ord(k[i % len(k)])) for i, c in enumerate(txt))
        print(f"  {CLR_PINK}Hex Result:{CLR_RESET} {res.encode('latin1', errors='ignore').hex()}")

def tool_54_base_encoders():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [54] Base16 (Hex), Base32 & Base64 Converter ==={CLR_RESET}")
    txt = input("  Enter text to encode: ").encode()
    print(f"  Base64: {base64.b64encode(txt).decode()}")
    print(f"  Base32: {base64.b32encode(txt).decode()}")
    print(f"  Base16: {base64.b16encode(txt).decode()}")

def tool_55_caesar_rot13():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [55] Caesar & ROT13 Substitution Cipher ==={CLR_RESET}")
    txt = input("  Enter string to apply ROT13: ")
    import codecs
    res = codecs.encode(txt, 'rot_13')
    print(f"  {CLR_GREEN}ROT13:{CLR_RESET} {res}")

def tool_56_password_matrix():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [56] High-Entropy Password & Token Matrix ==={CLR_RESET}")
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    pwd = "".join(secrets.choice(chars) for _ in range(24))
    token = secrets.token_hex(16)
    print(f"  {CLR_GREEN}Password:{CLR_RESET} {pwd}")
    print(f"  {CLR_GREEN}Token   :{CLR_RESET} {token}")

def tool_57_shannon_entropy():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [57] Shannon Entropy Password Strength Grader ==={CLR_RESET}")
    pwd = input("  Enter test password: ")
    pool = 0
    if any(c.islower() for c in pwd): pool += 26
    if any(c.isupper() for c in pwd): pool += 26
    if any(c.isdigit() for c in pwd): pool += 10
    if any(c in string.punctuation for c in pwd): pool += 32
    ent = len(pwd) * math.log2(pool) if pool else 0
    print(f"  {CLR_CYAN}Entropy: {ent:.1f} bits{CLR_RESET}")
    if ent > 70: print(f"  Rating: {CLR_GREEN}VERY STRONG{CLR_RESET}")
    elif ent > 50: print(f"  Rating: {CLR_YELLOW}MODERATE{CLR_RESET}")
    else: print(f"  Rating: {CLR_RED}WEAK{CLR_RESET}")

def tool_58_hmac_generator():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [58] HMAC SHA-256 Signature Generator ==={CLR_RESET}")
    msg = input("  Enter message: ").encode()
    key = input("  Enter HMAC key: ").encode()
    sig = hmac.new(key, msg, hashlib.sha256).hexdigest()
    print(f"  {CLR_GREEN}HMAC Signature:{CLR_RESET} {sig}")

def tool_59_random_dice():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [59] Cryptographic Random Numbers & Dice ==={CLR_RESET}")
    print(f"  Random Int (1-1000): {secrets.randbelow(1000) + 1}")
    print(f"  Dice Roll (1-6)    : {secrets.randbelow(6) + 1}")
    print(f"  Cryptographic Bytes: {secrets.token_hex(8)}")

def tool_60_uuid_gen():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [60] UUID / GUID Generator (v4 Cryptographic) ==={CLR_RESET}")
    for i in range(3):
        print(f"  GUID #{i+1}: {CLR_CYAN}{uuid.uuid4()}{CLR_RESET}")
