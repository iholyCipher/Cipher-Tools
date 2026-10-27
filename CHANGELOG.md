# Changelog

All notable changes to **Cipher Tools** are documented in this file.  
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-10-27

### Highlights

> **625 verified, production-grade cybersecurity, forensics, network telemetry, and system engineering engines — 100% pure Python standard library, zero external dependencies.**

### Added

- **625 Native Operational Tools** across **21 core disciplines**, completely implemented and self-contained with zero third-party pip dependencies.
- **Deep PE/COFF Binary Inspection Engine (Tool 74)**:
  - Step-by-step raw struct parser for `IMAGE_DOS_HEADER`, `e_lfanew`, `IMAGE_NT_HEADERS32`/`64`, and Optional Headers.
  - Complete Section Table parser computing Virtual Addresses, raw byte offsets, sizes, and mapping memory protection characteristics (`[R-X]`, `[RW-]`, `[R--]`).
- **Sliding-Window Shannon Entropy Scanner (Tool 75)**:
  - 512-byte sliding window analysis calculating entropy distribution profiles ($0.0 - 8.0$ bits/byte).
  - Automated heuristic classification tagging payloads as `PACKED / ENCRYPTED`, `EXECUTABLE CODE`, `STRUCTURED DATA`, or `SPARSE / ZERO PADDING`.
- **Mandiant Standard ImpHash Calculator (Tool 352)**:
  - Exact binary IAT/ILT parser resolving both ordinal imports and name-hint thunks.
  - Mandiant-compliant canonical ordering (`module.function` lowercased and sorted) producing verifiable MD5 import hashes for malware attribution.
- **Surgical PE Section Entropy Analyzer (Tool 354)**:
  - Calculates per-section Shannon entropy and flags packed or obfuscated executable segments exceeding the $7.2$ bits threshold.
- **AST-Based Static Application Security Testing (SAST) Scanner (Tool 581)**:
  - Python Abstract Syntax Tree (`ast.parse`) traversal engine detecting dangerous code constructs.
  - Rule-based vulnerability detection for Dynamic Code Execution (CWE-95: `eval`/`exec`), Command Injection (CWE-78: `os.system`/`subprocess`), Insecure Deserialization (CWE-502: `pickle.loads`), Weak Cryptography (CWE-327: `hashlib.md5`/`sha1`), and Hardcoded Secrets (CWE-798).
- **Raw TLS 1.3 ClientHello Binary Dissector & DPI Evasion Engine (Tool 611)**:
  - Dissects and constructs wire-format TLS Record / Handshake binaries.
  - Dissects Server Name Indication (SNI) extensions and computes exact byte split boundaries for TCP payload fragmentation past Deep Packet Inspection filters.
- **Deep Forensic Smart Data Carvers (Tools 490 & 492)**:
  - **JPEG Carver**: Extracts images scanning SOI (`0xFFD8`) to EOI (`0xFFD9`) while validating internal structural markers (APP0/JFIF, DQT, SOF, SOS) to prevent corrupt false-positive extraction.
  - **PDF Carver**: Extracts documents from raw byte streams from `%PDF-1.x` headers to `%%EOF`, validating cross-reference (`xref`) and catalog dictionary integrity.
- **Dual-Mode Execution Architecture**:
  - Interactive cyberpunk terminal interface (TUI) with category browsing and keyboard navigation.
  - Headless automation CLI with `--tool`, `--search`, `--category`, `--list`, `--json`, `--test`, and `--info`.
- **Automated Comprehensive QA Engine**:
  - `test_suite.py` delivering 100% verification across all 625 tools with mocked stdin and isolated environment execution.
- **Zero-Dependency Guarantee**: Runs on any clean Python 3.8+ installation on Windows, Linux, and macOS.

### Removed

- Purged placeholder stub tools (Tools 626–1250, Categories 22–35) to eliminate non-functional templates and ensure every single tool in the suite is authentic, robust, and functional.

### Disciplines (21 Categories)

| # | Category | Tools | Range | Description |
|:-:|:---|:---:|:---:|:---|
| 01 | System, OS & Kernel | 10 | 1–10 | Hardware architecture, OS build, system metrics, PATH integrity |
| 02 | CPU, Memory & Benchmarks | 10 | 11–20 | Synthetic CPU stress, matrix FLOPS, RAM bandwidth, process telemetry |
| 03 | Storage & Disk Forensics | 10 | 21–30 | Duplicate file detection, SHA-256 manifests, directory trees |
| 04 | Network Reconnaissance | 10 | 31–40 | ARP table sweeps, TCP port probing, DNS benchmark, routing tables |
| 05 | Web & OSINT | 10 | 41–50 | X.509 TLS certificate inspector, HTTP headers, redirect tracer |
| 06 | Cryptography & Hashing | 10 | 51–60 | Cryptographic hash engine, HMAC, Shannon entropy, XOR ciphers |
| 07 | Cybersecurity & Defense | 10 | 61–70 | Windows Firewall audit, password strength, DoD 5220.22-M file shredder |
| 08 | Binary Forensics | 10 | 71–80 | Deep PE parser, sliding entropy scanner, magic bytes, hex dumps |
| 09 | Windows Administration | 10 | 81–90 | Run/RunOnce persistence audit, service manager, event log inspector |
| 10 | Developer Utilities | 10 | 91–100 | RFC 8259 JSON validator, regex debugger, base conversions |
| 11 | Domestic Network & Censorship | 50 | 101–150 | DNS poisoning detection, TCP reset tracer, Cloudflare clean IP scanner |
| 12 | Data Science & Statistics | 50 | 151–200 | Matrix algebra, statistical moments, linear regression, K-Means |
| 13 | Advanced Cryptography | 50 | 201–250 | Feistel ciphers, Shamir secret sharing, PKCS#7, Diffie-Hellman |
| 14 | Firewall & Protocol Telemetry | 50 | 251–300 | Raw socket headers, TTL hop distance, TCP flags, ICMP diagnostics |
| 15 | Windows Internals | 30 | 301–330 | SAM/SYSTEM registry hives, WMI queries, ETW trace providers |
| 16 | Malware Analysis | 70 | 331–400 | Mandiant ImpHash, section entropy, Rich Header, YARA pattern matcher |
| 17 | Web Security & APIs | 50 | 401–450 | OWASP payload generators, CORS misconfiguration tester, JWT analyzer |
| 18 | Storage Forensics & Recovery | 50 | 451–500 | Smart JPEG/PDF carvers, Master File Table parser, NTFS streams |
| 19 | Hardware & Thermal | 50 | 501–550 | Thermal sensor telemetry, battery wear level, storage SMART diagnostics |
| 20 | Developer Swiss Army | 50 | 551–600 | AST SAST vulnerability scanner, SQL formatter, tokenizers, diff engines |
| 21 | Censorship Resilience | 25 | 601–625 | TLS 1.3 ClientHello dissector, SNI fragmentation, V2Ray/Xray config builder |
