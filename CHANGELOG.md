# Changelog

All notable changes to **Cipher Tools** are documented in this file.  
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-10-26

### Highlights

> **1,250 precision cybersecurity, forensics, and system engineering tools — zero external dependencies.**

### Added

- **1,250 Native Tools** organized across **35 engineering disciplines**, each fully implemented in pure Python standard library.
- **Modular Architecture** — 35 self-contained category modules under `modules/` with a centralized static registry (`modules/registry.py`) enabling sub-millisecond tool dispatch.
- **Dual-Mode Interface** — Interactive cyberpunk TUI with two-column category navigation *and* full headless CLI (`--tool`, `--search`, `--category`, `--list`, `--json`, `--test`, `--info`, `--version`).
- **Exhaustive Automated QA** — `test_suite.py` validates all 1,250 tools with mocked I/O, achieving a 100% pass rate.
- **GitHub Actions CI Pipeline** — Multi-version Python testing (3.8 through 3.13) on `windows-latest`.
- **Standard Packaging** — `pyproject.toml` (PEP 517/518), `setup.py`, `requirements.txt`, `LICENSE` (MIT), and `CONTRIBUTING.md`.
- **JSON Export** — Machine-readable full catalog via `--json` for integrations, dashboards, and automation scripts.

### Disciplines (35 Categories)

| # | Category | Tools | Description |
|:-:|:---|:---:|:---|
| 1 | System, OS & Kernel | 1–10 | Uptime, hotfixes, PATH validation, kernel build info |
| 2 | CPU, Memory & Benchmarks | 11–20 | FLOPs, integer stress, RAM bandwidth, process hierarchy |
| 3 | Storage & Disk Forensics | 21–30 | Duplicate finder, checksum manifests, zero-byte scanner |
| 4 | Network Reconnaissance | 31–40 | ARP sweep, port scanner, DNS benchmark, routing table |
| 5 | Web & OSINT | 41–50 | SSL inspector, header grabber, redirect tracker |
| 6 | Cryptography & Hashing | 51–60 | Multi-hash, XOR cipher, Shannon entropy, HMAC |
| 7 | Cybersecurity & Defense | 61–70 | Firewall status, password auditor, file shredder |
| 8 | Binary Forensics | 71–80 | Hex viewer, magic bytes, PE analyzer, entropy calc |
| 9 | Windows Administration | 81–90 | Startup persistence, services, event logs, defender |
| 10 | Developer Utilities | 91–100 | JSON validator, regex tester, base converter |
| 11 | Domestic Network & Censorship | 101–150 | DNS benchmark, DPI detection, Cloudflare IP scanner |
| 12 | Data Science & Statistics | 151–200 | Matrix ops, distributions, regression, clustering |
| 13 | Advanced Cryptography | 201–250 | AES/RSA specs, key exchange, certificate parsing |
| 14 | Firewall & Protocol Telemetry | 251–300 | SYN flood sim, TLS ALPN, DNSSEC, packet TTL |
| 15 | Windows Internals | 301–330 | Registry hives, WMI, ETW, driver signing |
| 16 | Malware Analysis | 331–400 | PE/ELF/Mach-O headers, Rich hash, YARA patterns |
| 17 | Web Security & APIs | 401–450 | XSS/SQLi payloads, CORS audit, JWT cracker |
| 18 | Storage Forensics & Recovery | 451–500 | File carving, BOM detection, NTFS compression |
| 19 | Hardware & Thermal | 501–550 | GPU telemetry, battery health, fan/thermal probes |
| 20 | Developer Swiss Army | 551–600 | Code formatters, linters, diff engines |
| 21 | Censorship Resilience | 601–625 | SNI fragmentation, v2ray configs, VPN killswitch |
| 22 | Active Directory & Kerberos | 626–675 | TGT/TGS analysis, LDAP filters, BloodHound, DPAPI |
| 23 | Cloud & Kubernetes | 676–725 | AWS IAM linter, K8s PSS, Docker rootless audit |
| 24 | Linux Internals | 726–775 | SUID/SGID hunter, PAM auditor, SELinux/AppArmor |
| 25 | Offensive Defense | 776–825 | AMSI bypass, LOLBAS catalog, Sysmon linter, YARA |
| 26 | Deep Protocol Analysis | 826–875 | DNS/DHCP/BGP/OSPF/Kerberos/SMB/RDP decoders |
| 27 | Web3 & Blockchain | 876–925 | EVM disassembler, Solidity SWC, ERC standards |
| 28 | Wireless & RF | 926–975 | 802.11 frames, WPA3 handshake, BLE, Zigbee, LoRa |
| 29 | Threat Hunting & OSINT | 976–1025 | MITRE ATT&CK mapper, IOC extraction, Magecart |
| 30 | Incident Response | 1026–1075 | Shimcache, Amcache, Prefetch, Shellbags, crash dumps |
| 31 | APIs & Microservices | 1076–1125 | GraphQL introspection, gRPC/Protobuf, OpenAPI lint |
| 32 | DevSecOps & SAST | 1126–1175 | Git secret scanner, SBOM, Semgrep rules, CI/CD audit |
| 33 | Database Security | 1176–1210 | SQL injection sim, Redis/MongoDB/Kafka/Snowflake audit |
| 34 | Quantum Cryptography | 1211–1235 | NIST PQC (Kyber/Dilithium), Shor/Grover estimators |
| 35 | Autonomous AI & LLM Security | 1236–1250 | Prompt injection, RAG chunking, OWASP LLM Top 10 |

### Technical Specifications

- **Python**: 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, 3.14+
- **Dependencies**: Zero mandatory pip packages
- **Platforms**: Windows x64, Linux, macOS
- **License**: MIT
