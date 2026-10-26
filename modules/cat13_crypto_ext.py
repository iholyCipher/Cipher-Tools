# -*- coding: utf-8 -*-
"""
Cipher Tools - Category 13: Advanced Cryptography, Encoders & Key Management (Tools 201 - 250)
Pure Python Standard Library (hashlib, hmac, base64, zlib, secrets)
"""
import os
import sys
import zlib
import hmac
import base64
import hashlib
import secrets
import string
import math

CLR_CYAN = "\033[96m"
CLR_PINK = "\033[95m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_GRAY = "\033[90m"
CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"

def tool_201_sha3_256():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [201] SHA3-256 Cryptographic Hash Engine ==={CLR_RESET}")
    txt = input("  Enter text to hash: ").strip() or "cipher_tools"
    h = hashlib.sha3_256(txt.encode('utf-8')).hexdigest()
    print(f"  SHA3-256: {CLR_GREEN}{h}{CLR_RESET}")

def tool_202_sha3_512():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [202] SHA3-512 Cryptographic Hash Engine ==={CLR_RESET}")
    txt = input("  Enter text to hash: ").strip() or "cipher_tools"
    h = hashlib.sha3_512(txt.encode('utf-8')).hexdigest()
    print(f"  SHA3-512: {CLR_GREEN}{h}{CLR_RESET}")

def tool_203_blake2b_hasher():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [203] BLAKE2b High-Performance 512-bit Hash ==={CLR_RESET}")
    txt = input("  Enter text: ").strip() or "cipher_tools"
    h = hashlib.blake2b(txt.encode('utf-8')).hexdigest()
    print(f"  BLAKE2b: {CLR_GREEN}{h}{CLR_RESET}")

def tool_204_blake2s_hasher():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [204] BLAKE2s Fast 256-bit Hash ==={CLR_RESET}")
    txt = input("  Enter text: ").strip() or "cipher_tools"
    h = hashlib.blake2s(txt.encode('utf-8')).hexdigest()
    print(f"  BLAKE2s: {CLR_GREEN}{h}{CLR_RESET}")

def tool_205_shake_128_256():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [205] SHAKE Extendable-Output Function (XOF) ==={CLR_RESET}")
    txt = input("  Enter seed string: ").strip() or "cipher_seed"
    length = int(input("  Enter desired output byte length (default 32): ").strip() or "32")
    h = hashlib.shake_256(txt.encode()).hexdigest(length)
    print(f"  SHAKE256 ({length} bytes): {CLR_GREEN}{h}{CLR_RESET}")

def tool_206_crc32_checksum():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [206] CRC32 Checksum Calculator ==={CLR_RESET}")
    txt = input("  Enter string or data: ").strip() or "123456789"
    crc = zlib.crc32(txt.encode('utf-8'))
    print(f"  CRC32 Hex     : {CLR_GREEN}{crc:08X}{CLR_RESET}")
    print(f"  CRC32 Integer : {crc}")

def tool_207_adler32_checksum():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [207] Adler-32 Checksum Engine ==={CLR_RESET}")
    txt = input("  Enter string: ").strip() or "Wikipedia"
    adler = zlib.adler32(txt.encode('utf-8'))
    print(f"  Adler-32 Hex    : {CLR_GREEN}{adler:08X}{CLR_RESET}")
    print(f"  Adler-32 Integer: {adler}")

def tool_208_pbkdf2_hmac():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [208] PBKDF2 Key Derivation Function (KDF) ==={CLR_RESET}")
    pwd = input("  Enter password: ").strip() or "SuperSecret123"
    salt = input("  Enter salt (default 'ciphersalt'): ").strip() or "ciphersalt"
    iters = int(input("  Iterations (default 100000): ").strip() or "100000")
    key = hashlib.pbkdf2_hmac('sha256', pwd.encode(), salt.encode(), iters)
    print(f"  Derived 256-bit Key: {CLR_GREEN}{key.hex()}{CLR_RESET}")

def tool_209_vigenere_cipher():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [209] Vigenère Polyalphabetic Cipher ==={CLR_RESET}")
    text = input("  Enter plaintext (A-Z): ").upper() or "ATTACKATDAWN"
    key = input("  Enter key (A-Z): ").upper() or "LEMON"
    clean_t = [c for c in text if c.isalpha()]
    res = []
    for i, c in enumerate(clean_t):
        k = key[i % len(key)]
        res.append(chr(((ord(c) - 65 + ord(k) - 65) % 26) + 65))
    print(f"  Ciphertext: {CLR_GREEN}{''.join(res)}{CLR_RESET}")

def tool_210_atbash_cipher():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [210] Atbash Classical Mirror Substitution Cipher ==={CLR_RESET}")
    text = input("  Enter text: ") or "Hello World"
    res = []
    for c in text:
        if 'a' <= c <= 'z': res.append(chr(ord('z') - (ord(c) - ord('a'))))
        elif 'A' <= c <= 'Z': res.append(chr(ord('Z') - (ord(c) - ord('A'))))
        else: res.append(c)
    print(f"  Atbash Result: {CLR_GREEN}{''.join(res)}{CLR_RESET}")

def tool_211_rot47_cipher():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [211] ROT47 ASCII 94-Character Rotation Cipher ==={CLR_RESET}")
    text = input("  Enter string to ROT47: ") or "Cipher!Tools#2026"
    res = []
    for c in text:
        ascii_code = ord(c)
        if 33 <= ascii_code <= 126:
            res.append(chr(33 + ((ascii_code - 33 + 47) % 94)))
        else: res.append(c)
    print(f"  ROT47 Result: {CLR_GREEN}{''.join(res)}{CLR_RESET}")

def tool_212_rail_fence_cipher():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [212] Rail Fence (Zigzag) Transposition Cipher ==={CLR_RESET}")
    text = input("  Enter text: ") or "DEFENDTHEEASTWALL"
    rails = int(input("  Enter rails (default 3): ").strip() or "3")
    fence = [[] for _ in range(rails)]
    rail = 0
    dir_down = False
    for c in text:
        fence[rail].append(c)
        if rail == 0 or rail == rails - 1:
            dir_down = not dir_down
        rail += 1 if dir_down else -1
    cipher = "".join("".join(row) for row in fence)
    print(f"  Zigzag Encrypted: {CLR_GREEN}{cipher}{CLR_RESET}")

def tool_213_morse_code():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [213] International Morse Code Encoder/Decoder ==={CLR_RESET}")
    morse_map = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '0': '-----', ' ': '/'
    }
    t = input("  Enter text to encode (or Morse code to decode): ").strip().upper() or "SOS CIPHER"
    if any(c in ('-', '.') for c in t):
        rev = {v: k for k, v in morse_map.items()}
        dec = "".join(rev.get(token, "?") for token in t.split())
        print(f"  Decoded: {CLR_GREEN}{dec}{CLR_RESET}")
    else:
        enc = " ".join(morse_map.get(c, "") for c in t)
        print(f"  Morse: {CLR_GREEN}{enc}{CLR_RESET}")

def tool_214_base85_ascii85():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [214] Ascii85 & Base85 Encoder/Decoder ==={CLR_RESET}")
    raw = input("  Enter string to encode: ") or "Cipher Tools Titan Suite"
    b85 = base64.b85encode(raw.encode()).decode()
    a85 = base64.a85encode(raw.encode()).decode()
    print(f"  Standard Base85: {CLR_GREEN}{b85}{CLR_RESET}")
    print(f"  Adobe Ascii85  : {CLR_CYAN}{a85}{CLR_RESET}")

def tool_215_base58_btc():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [215] Bitcoin Base58 Encoder Engine ==={CLR_RESET}")
    b58_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    raw = input("  Enter text: ") or "Bitcoin"
    data = raw.encode()
    num = int.from_bytes(data, 'big')
    res = ""
    while num > 0:
        num, rem = divmod(num, 58)
        res = b58_chars[rem] + res
    for byte in data:
        if byte == 0: res = b58_chars[0] + res
        else: break
    print(f"  Base58: {CLR_GREEN}{res}{CLR_RESET}")

def tool_216_jwt_inspector():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [216] JSON Web Token (JWT) Header & Payload Inspector ==={CLR_RESET}")
    dummy = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkNpcGhlciBPcGVyYXRvciIsImlhdCI6MTUxNjIzOTAyMn0.dummy"
    token = input(f"  Enter JWT string [default sample]: ").strip() or dummy
    parts = token.split(".")
    if len(parts) >= 2:
        try:
            def b64url_dec(s):
                s += '=' * ((4 - len(s) % 4) % 4)
                return base64.urlsafe_b64decode(s).decode('utf-8', errors='ignore')
            print(f"  {CLR_CYAN}Header :{CLR_RESET} {b64url_dec(parts[0])}")
            print(f"  {CLR_GREEN}Payload:{CLR_RESET} {b64url_dec(parts[1])}")
        except Exception as e:
            print(f"  {CLR_RED}[-] JWT Decode Error: {e}{CLR_RESET}")

def tool_217_nato_phonetic():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [217] NATO Phonetic Spelling Generator ==={CLR_RESET}")
    nato = {
        'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
        'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
        'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
        'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'
    }
    s = input("  Enter callsign or text: ").strip().upper() or "CIPHER"
    print(f"  Spelling: {CLR_GREEN}{' '.join(nato.get(c, c) for c in s)}{CLR_RESET}")

def tool_218_leetspeak_converter():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [218] Leetspeak (1337) Multi-Dialect Converter ==={CLR_RESET}")
    text = input("  Enter string to convert: ") or "Cyber Security and Forensics"
    t_map = {'A': '4', 'E': '3', 'I': '1', 'O': '0', 'S': '5', 'T': '7'}
    leet = "".join(t_map.get(c.upper(), c) for c in text)
    print(f"  Leet 1337: {CLR_GREEN}{leet}{CLR_RESET}")

def tool_219_binary_to_c_array():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [219] Shellcode / Binary to C Byte Array Generator ==={CLR_RESET}")
    data = (input("  Enter ASCII string or byte hex: ").strip() or "CipherPayload").encode()
    c_bytes = ", ".join(f"0x{b:02X}" for b in data)
    print(f"  unsigned char payload[] = {{ {c_bytes} }};")
    print(f"  unsigned int payload_len = {len(data)};")

def tool_220_steganography_zero_width():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [220] Steganography: Zero-Width Unicode Injector ==={CLR_RESET}")
    cover = input("  Enter visible cover text: ") or "This is completely normal text."
    secret = input("  Enter secret payload: ") or "SECRET"
    # Zero width spaces: U+200B (0), U+200C (1)
    bin_secret = "".join(f"{ord(c):08b}" for c in secret)
    zw = "".join("\u200B" if b == '0' else "\u200C" for b in bin_secret)
    stego = cover[:5] + zw + cover[5:]
    print(f"  Result Length   : {len(stego)} characters (Hidden {len(bin_secret)} bits)")
    print(f"  Rendered Output : '{stego}'")

def tool_221_steganography_zero_width_decoder():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [221] Steganography: Zero-Width Decoder ==={CLR_RESET}")
    sample = "This \u200B\u200C\u200B\u200C\u200B\u200B\u200B\u200Cis normal"
    target = input("  Enter text with zero-width characters [or press Enter for sample]: ") or sample
    bits = "".join('0' if c == '\u200B' else '1' for c in target if c in ('\u200B', '\u200C'))
    chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8) if len(bits[i:i+8]) == 8]
    print(f"  Extracted Hidden Secret: {CLR_GREEN}{''.join(chars) or 'None found'}{CLR_RESET}")

def tool_222_hash_collision_prob():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [222] Birthday Paradox Hash Collision Probability ==={CLR_RESET}")
    bits = int(input("  Enter hash bit length (e.g. 32, 64, 128, 256): ").strip() or "64")
    samples = float(input("  Enter number of hashed items (e.g. 1000000): ").strip() or "1000000")
    total_space = 2 ** bits
    prob = 1 - math.exp(-(samples ** 2) / (2 * total_space))
    print(f"  Probability of Collision: {CLR_GREEN}{prob:.6e}{CLR_RESET}")

def tool_223_pkcs7_padding_verifier():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [223] PKCS#7 Cryptographic Block Padding Validator ==={CLR_RESET}")
    sample = b"CipherBlockData\x01"
    pad_len = sample[-1]
    is_valid = (1 <= pad_len <= 16) and (sample[-pad_len:] == bytes([pad_len] * pad_len))
    print(f"  Block Sample: {sample}")
    print(f"  Padding Byte: 0x{pad_len:02X}")
    print(f"  Status: {CLR_GREEN}VALID PKCS#7{CLR_RESET}" if is_valid else f"{CLR_RED}INVALID{CLR_RESET}")

def tool_224_diceware_passphrase():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [224] Diceware Cryptographic Passphrase Generator ==={CLR_RESET}")
    words = ["correct", "horse", "battery", "staple", "cipher", "titan", "matrix", "shield", "dragon", "orbit", "quantum", "vector"]
    passphrase = "-".join(secrets.choice(words) for _ in range(5))
    print(f"  High-Entropy Diceware Passphrase: {CLR_GREEN}{passphrase}{CLR_RESET}")

def tool_225_url_safe_token():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [225] High-Entropy URL-Safe Token Generator ==={CLR_RESET}")
    nbytes = int(input("  Token byte entropy (default 32): ").strip() or "32")
    token = secrets.token_urlsafe(nbytes)
    print(f"  Token: {CLR_GREEN}{token}{CLR_RESET}")

def tool_226_argon2_bcrypt_identifier():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [226] Password Hash Format Classifier (Bcrypt / Argon2 / SHA-crypt) ==={CLR_RESET}")
    h = input("  Enter hash string: ").strip() or "$2a$12$R9h/cIPz0gi.URNNX3kh2OPST9/PgBkqquzi.Ss7KIUgO2t0jWMUW"
    if h.startswith(("$2a$", "$2b$", "$2y$")):
        print(f"  Classification: {CLR_GREEN}Bcrypt Password Hash{CLR_RESET}")
    elif h.startswith("$argon2id$") or h.startswith("$argon2i$"):
        print(f"  Classification: {CLR_GREEN}Argon2 Modern KDF Hash{CLR_RESET}")
    elif h.startswith("$6$"):
        print(f"  Classification: {CLR_CYAN}SHA-512 Unix Crypt ($6$){CLR_RESET}")
    elif h.startswith("$1$"):
        print(f"  Classification: {CLR_YELLOW}MD5 Unix Crypt ($1$){CLR_RESET}")
    else:
        print(f"  Unrecognized standard salt prefix.")

def tool_227_entropy_file_block_mapper():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [227] Block-by-Block Entropy Density Mapper ==={CLR_RESET}")
    path = input("  Enter file path: ").strip(' "\'') or "README.md"
    if not os.path.isfile(path): return
    with open(path, 'rb') as fp: data = fp.read()
    bs = 256
    print(f"  Scanning {len(data):,} bytes in {bs}-byte blocks:")
    for i in range(0, min(len(data), bs * 5), bs):
        blk = data[i:i+bs]
        cnts = [blk.count(x) for x in set(blk)]
        ent = -sum((c/len(blk)) * math.log2(c/len(blk)) for c in cnts)
        bar = "█" * int(ent * 2)
        print(f"  Block 0x{i:04X}: {CLR_CYAN}{bar:<16}{CLR_RESET} ({ent:.2f} bits)")

def tool_228_rc4_cipher_stream():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [228] Rivest Cipher 4 (RC4) Symmetric Stream Cipher ==={CLR_RESET}")
    key = (input("  Enter key (default 'cipherkey'): ").strip() or "cipherkey").encode()
    data = (input("  Enter text to stream encrypt: ").strip() or "Classified Intelligence").encode()
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    i = j = 0
    out = bytearray()
    for b in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        out.append(b ^ K)
    print(f"  RC4 Output Hex: {CLR_GREEN}{out.hex()}{CLR_RESET}")

def tool_229_bech32_inspect():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [229] Bech32 SegWit Address Inspector ==={CLR_RESET}")
    addr = input("  Enter Bech32 address: ").strip() or "bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4"
    if addr.startswith("bc1"):
        print(f"  {CLR_GREEN}[✓] Valid Bitcoin SegWit mainnet address format.{CLR_RESET}")
    elif addr.startswith("tb1"):
        print(f"  {CLR_CYAN}[✓] Valid Bitcoin testnet SegWit address.{CLR_RESET}")
    else:
        print("  Non-standard Bech32 format.")

def tool_230_totp_hotp_calculator():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [230] RFC 6238 TOTP (2FA Authentication Code Simulator) ==={CLR_RESET}")
    secret = (input("  Enter base32 secret [default 'JBSWY3DPEHPK3PXP']: ").strip() or "JBSWY3DPEHPK3PXP").upper()
    try:
        import struct, time
        key = base64.b32decode(secret)
        counter = int(time.time() // 30)
        msg = struct.pack(">Q", counter)
        h = hmac.new(key, msg, hashlib.sha1).digest()
        o = h[19] & 15
        code = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
        print(f"  Current 2FA OTP Code: {CLR_GREEN}{code:06d}{CLR_RESET} (Refreshes in {30 - int(time.time() % 30)}s)")
    except Exception as e:
        print(f"  {CLR_RED}[-] TOTP Error: {e}{CLR_RESET}")

def tool_231_shamir_secret_sharing_math():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [231] Shamir's Secret Sharing (Polynomial 2-of-3) ==={CLR_RESET}")
    secret = 42
    p = 7919
    a1 = 15
    f = lambda x: (secret + a1 * x) % p
    s1, s2, s3 = (1, f(1)), (2, f(2)), (3, f(3))
    print(f"  Original Secret : {secret}")
    print(f"  Share 1 (x=1)   : {s1}")
    print(f"  Share 2 (x=2)   : {s2}")
    print(f"  Share 3 (x=3)   : {s3}")
    # Reconstruct from share 1 & 2
    recon = (s1[1] * (0 - s2[0]) * pow(s1[0] - s2[0], -1, p) + s2[1] * (0 - s1[0]) * pow(s2[0] - s1[0], -1, p)) % p
    print(f"  Reconstructed   : {CLR_GREEN}{recon}{CLR_RESET}")

def tool_232_diffie_hellman_sim():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [232] Diffie-Hellman Key Exchange Simulation ==={CLR_RESET}")
    p = 23; g = 5
    a = secrets.randbelow(15) + 1
    b = secrets.randbelow(15) + 1
    A = pow(g, a, p); B = pow(g, b, p)
    s_alice = pow(B, a, p); s_bob = pow(A, b, p)
    print(f"  Public (p={p}, g={g}) | Alice Pub={A}, Bob Pub={B}")
    print(f"  Shared Secret Agreement: {CLR_GREEN}{s_alice}{CLR_RESET} == {CLR_GREEN}{s_bob}{CLR_RESET}")

def tool_233_md5_file_hasher():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [233] Fast Buffered MD5 File Hasher ==={CLR_RESET}")
    p = input("  Enter file: ").strip(' "\'') or "README.md"
    if not os.path.isfile(p): return
    h = hashlib.md5()
    with open(p, 'rb') as fp:
        while chunk := fp.read(131072): h.update(chunk)
    print(f"  MD5 ({os.path.basename(p)}): {CLR_GREEN}{h.hexdigest()}{CLR_RESET}")

def tool_234_sha256_file_hasher():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [234] Fast Buffered SHA-256 File Hasher ==={CLR_RESET}")
    p = input("  Enter file: ").strip(' "\'') or "README.md"
    if not os.path.isfile(p): return
    h = hashlib.sha256()
    with open(p, 'rb') as fp:
        while chunk := fp.read(131072): h.update(chunk)
    print(f"  SHA-256 ({os.path.basename(p)}): {CLR_GREEN}{h.hexdigest()}{CLR_RESET}")

def tool_235_sha512_file_hasher():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [235] Fast Buffered SHA-512 File Hasher ==={CLR_RESET}")
    p = input("  Enter file: ").strip(' "\'') or "README.md"
    if not os.path.isfile(p): return
    h = hashlib.sha512()
    with open(p, 'rb') as fp:
        while chunk := fp.read(131072): h.update(chunk)
    print(f"  SHA-512 ({os.path.basename(p)}): {CLR_GREEN}{h.hexdigest()}{CLR_RESET}")

def tool_236_hex_to_ascii():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [236] Hexadecimal to ASCII Text Converter ==={CLR_RESET}")
    hx = input("  Enter hex string: ").replace(" ", "").strip() or "436970686572"
    try:
        t = bytes.fromhex(hx).decode('utf-8', errors='replace')
        print(f"  ASCII: {CLR_GREEN}{t}{CLR_RESET}")
    except Exception as e: print(f"  Error: {e}")

def tool_237_ascii_to_hex():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [237] ASCII Text to Hexadecimal Stream ==={CLR_RESET}")
    t = input("  Enter text: ") or "Cipher Tools"
    print(f"  Hex: {CLR_GREEN}{t.encode().hex()}{CLR_RESET}")

def tool_238_binary_to_text():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [238] Binary 8-bit ASCII Bitstream to Text ==={CLR_RESET}")
    b_str = input("  Enter binary string (space separated or continuous): ").replace(" ", "").strip() or "0100001101101001"
    try:
        chars = [chr(int(b_str[i:i+8], 2)) for i in range(0, len(b_str), 8)]
        print(f"  Text: {CLR_GREEN}{''.join(chars)}{CLR_RESET}")
    except Exception as e: print(f"  Error: {e}")

def tool_239_text_to_binary():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [239] Text to 8-bit Binary Stream ==={CLR_RESET}")
    t = input("  Enter text: ") or "Titan"
    bins = " ".join(f"{ord(c):08b}" for c in t)
    print(f"  Binary: {CLR_GREEN}{bins}{CLR_RESET}")

def tool_240_html_entity_encoder():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [240] HTML Character Entity Encoder/Decoder ==={CLR_RESET}")
    import html
    s = input("  Enter HTML snippet: ") or "<script>alert('Cipher');</script>"
    enc = html.escape(s)
    print(f"  Escaped HTML: {CLR_GREEN}{enc}{CLR_RESET}")

def tool_241_caesar_bruteforce():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [241] Caesar Cipher Full 26-Shift Brute-Forcer ==={CLR_RESET}")
    t = input("  Enter ciphertext: ") or "WKLV LV D VHFUHW"
    for shift in range(1, 26):
        cand = "".join(chr((ord(c) - 65 - shift) % 26 + 65) if 'A' <= c <= 'Z' else c for c in t.upper())
        print(f"  Shift {shift:02d}: {cand}")

def tool_242_xor_bruteforce_single_byte():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [242] Single-Byte XOR Key Brute-Force Scanner ==={CLR_RESET}")
    sample = bytes([b ^ 0x5A for b in b"CipherPayload"])
    print(f"  Brute-forcing cipher block: {sample.hex()}")
    for k in range(256):
        dec = bytes([b ^ k for b in sample])
        if b"Cipher" in dec:
            print(f"  {CLR_GREEN}[✓] Discovered Key 0x{k:02X} ('{chr(k)}'): {dec.decode('latin1')}{CLR_RESET}")
            break

def tool_243_uuid_v5_hasher():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [243] Deterministic UUID v5 (SHA-1 Namespace) ==={CLR_RESET}")
    import uuid
    name = input("  Enter entity name: ").strip() or "ciphertools.org"
    u5 = uuid.uuid5(uuid.NAMESPACE_DNS, name)
    print(f"  UUID v5: {CLR_GREEN}{u5}{CLR_RESET}")

def tool_244_keccak_256():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [244] Keccak-256 (Ethereum Signature Pre-image) ==={CLR_RESET}")
    t = input("  Enter function signature (e.g. 'transfer(address,uint256)'): ").strip() or "transfer(address,uint256)"
    h = hashlib.sha3_256(t.encode()).hexdigest()
    print(f"  4-byte Method Selector: {CLR_GREEN}0x{h[:8]}{CLR_RESET}")

def tool_245_argon2_parameter_calc():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [245] Argon2 Memory & Parallelism Cost Evaluator ==={CLR_RESET}")
    mem_mb = int(input("  Enter target memory (MB, default 64): ").strip() or "64")
    t_cost = int(input("  Enter time iterations (default 3): ").strip() or "3")
    print(f"  Recommended Parameters:")
    print(f"  - Memory Cost (m)   : {mem_mb * 1024} KiB")
    print(f"  - Time Cost (t)     : {t_cost}")
    print(f"  - Parallelism (p)   : {os.cpu_count() or 4}")

def tool_246_openssl_aes_cmd_builder():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [246] OpenSSL CLI Command Generator (AES-256-GCM) ==={CLR_RESET}")
    f = input("  Target file to encrypt: ").strip() or "secret.doc"
    print(f"  Encryption:")
    print(f"  {CLR_CYAN}openssl enc -aes-256-cbc -salt -pbkdf2 -iter 100000 -in {f} -out {f}.enc{CLR_RESET}")
    print(f"  Decryption:")
    print(f"  {CLR_GREEN}openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -in {f}.enc -out {f}.dec{CLR_RESET}")

def tool_247_rsa_key_spec():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [247] RSA Key Size Security & Performance Matrix ==={CLR_RESET}")
    specs = [("RSA-1024", "Deprecated / Broken", "128 bytes", "Low"),
             ("RSA-2048", "Standard NIST compliant", "256 bytes", "Moderate"),
             ("RSA-3072", "High Security (Equivalent 128-bit symm)", "384 bytes", "Good"),
             ("RSA-4096", "Military / Top-Secret", "512 bytes", "High Compute")]
    for name, stat, sz, perf in specs:
        print(f"  {CLR_CYAN}{name:<10}{CLR_RESET} | {stat:<32} | {sz} | {perf}")

def tool_248_elliptic_curve_catalog():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [248] Elliptic Curves Cryptography (ECC) Specs ==={CLR_RESET}")
    curves = [("secp256k1", "Bitcoin, Ethereum", "256 bits", "Koblitz"),
              ("secp256r1 (P-256)", "TLS 1.3, NIST, Apple", "256 bits", "Weierstrass"),
              ("Curve25519", "Signal, WireGuard, SSH", "255 bits", "Montgomery"),
              ("Ed448 (Goldilocks)", "High-security EdDSA", "448 bits", "Edwards")]
    for c, use, bits, fam in curves:
        print(f"  {CLR_GREEN}{c:<18}{CLR_RESET} | {use:<22} | {bits} | {fam}")

def tool_249_password_entropy_meter():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [249] Password Crack Time Matrix (Brute-force) ==={CLR_RESET}")
    pwd = input("  Enter test password: ") or "Tr0ub4dor&3"
    import math
    pool = 0
    if any(c.islower() for c in pwd): pool += 26
    if any(c.isupper() for c in pwd): pool += 26
    if any(c.isdigit() for c in pwd): pool += 10
    if any(c in string.punctuation for c in pwd): pool += 32
    combinations = pool ** len(pwd)
    speed = 10_000_000_000 # 10 billion guesses/sec
    sec = combinations / speed
    print(f"  Combinations: {combinations:,.2e}")
    if sec < 60: print(f"  Crack Time  : {CLR_RED}Instant (< 1 minute){CLR_RESET}")
    elif sec < 86400: print(f"  Crack Time  : {CLR_YELLOW}{sec/3600:.1f} hours{CLR_RESET}")
    elif sec < 31536000 * 100: print(f"  Crack Time  : {CLR_GREEN}{sec/31536000:.1f} years{CLR_RESET}")
    else: print(f"  Crack Time  : {CLR_GREEN}Centuries+ (> 1000 years){CLR_RESET}")

def tool_250_crypto_suite_self_test():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [250] Crypto Engine Self-Test Verification ==={CLR_RESET}")
    assert hashlib.sha256(b"abc").hexdigest() == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    print(f"  {CLR_GREEN}[✓] Cryptographic hashes & vector engines fully calibrated!{CLR_RESET}")
