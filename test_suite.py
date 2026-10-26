#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cipher Tools - Titan Suite Automated Test & Quality Assurance Engine
Runs and validates all 150 tools one by one with safe mocked inputs.
"""

import os
import sys
import time
import io
from unittest.mock import patch

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, "modules"))

from cipher_tools import TOOLS, CATEGORIES

# Default safe mock inputs for tools that require user interaction
SAFE_MOCKS = {
    # Cat 1
    10: ["1"],  # abort timer option
    # Cat 2
    18: ["999999"],  # kill proc non-existent dummy PID
    # Cat 3
    22: ["."],  # dup finder
    23: ["."],  # folder tree
    24: ["."],  # empty pruner
    25: ["test", "1"],  # archive extractor
    26: [".", ".none1", ".none2"],  # batch rename
    27: ["."],  # manifest
    28: ["."],  # verify manifest
    29: ["."],  # zero byte
    30: ["."],  # largest files
    # Cat 4
    32: ["127.0.0.1"],  # port scanner
    33: ["127.0.0.1"],  # ping
    38: ["localhost"],  # reverse dns
    # Cat 5
    42: ["https://example.com"],  # headers
    43: ["google.com"],  # ssl cert
    44: ["https://example.com"],  # status
    45: [""],  # url dl empty
    46: ["example.com"],  # robots
    47: ["https://example.com"],  # redirect
    48: ["https://example.com"],  # meta
    49: ["example.com"],  # whois
    # Cat 6
    51: ["cipher_test_data"],  # multi hash
    52: ["d41d8cd98f00b204e9800998ecf8427e"],  # md5
    53: ["secret_message", "key123"],  # xor
    54: ["hello cipher"],  # base
    55: ["cipher rot13"],  # rot13
    57: ["StrongPassw0rd!#"],  # shannon
    58: ["test message", "secretkey"],  # hmac
    # Cat 7
    61: ["dummy_nonexistent_file.tmp", "no"],  # shredder
    68: ["."],  # ads
    # Cat 8
    71: ["README.md"],  # hex viewer
    72: ["README.md"],  # magic bytes
    73: ["README.md"],  # string extract
    74: ["README.md"],  # pe header
    75: ["README.md"],  # entropy
    76: ["README.md", "README.md"],  # diff
    77: ["README.md"],  # b64 in binary
    78: ["README.md"],  # regex in binary
    79: ["README.md"],  # timestomp
    80: ["README.md"],  # mime
    # Cat 10
    91: [""],  # epoch current
    92: ['{"status": "ok", "tools": 150}'],  # json
    93: ["<p>Hello <b>World</b></p>"],  # xml
    94: ["24"],  # cidr
    95: ["255"],  # base
    96: ["Cipher Tools Titan Suite provides 150 tools."],  # words
    97: ["Hello world cipher tools"],  # case
    98: ["# Header\n**Bold** and *italic* text"],  # md
    99: [r"\d+", "Found 150 tools in 2026."],  # regex
    100: ["1"],  # scratchpad view
    # Cat 11
    146: [""],  # sublink fetcher empty
    149: ["n"],  # tcp optimizer decline
}

def run_all_tests():
    total = len(TOOLS)
    passed = 0
    failed = 0
    errors = []

    print(f"\n====================================================================")
    print(f"🚀 CIPHER TOOLS - EXHAUSTIVE 150-TOOL QUALITY ASSURANCE SUITE")
    print(f"====================================================================\n")

    start_time = time.time()

    for tid in range(1, total + 1):
        name, func, cat = TOOLS[tid]
        mock_inputs = iter(SAFE_MOCKS.get(tid, ["\n", "", "1", "no", "n", "."]))
        
        # Intercept stdout so the test run is clean and concise
        captured_out = io.StringIO()
        t0 = time.time()

        try:
            with patch('builtins.input', lambda *args, **kwargs: next(mock_inputs, "")):
                with patch('sys.stdout', captured_out):
                    func()
            elapsed = time.time() - t0
            passed += 1
            print(f"  [✓] Tool {tid:03d} PASSED ({elapsed:.3f}s) | {cat:<10} | {name}")
        except Exception as e:
            elapsed = time.time() - t0
            failed += 1
            err_msg = str(e)
            errors.append((tid, name, cat, err_msg))
            print(f"  [✗] Tool {tid:03d} FAILED ({elapsed:.3f}s) | {cat:<10} | {name}: {err_msg}")

    total_time = time.time() - start_time
    print(f"\n====================================================================")
    print(f"TEST RESULTS SUMMARY:")
    print(f"  Total Tools Tested : {total}")
    print(f"  Passed             : {passed} ({(passed/total)*100:.1f}%)")
    print(f"  Failed             : {failed}")
    print(f"  Total Time         : {total_time:.2f} seconds")
    print(f"====================================================================")

    if errors:
        print("\nFailures to debug:")
        for tid, name, cat, err in errors:
            print(f"  - Tool #{tid} ({name}): {err}")
        return False
    else:
        print("\n🌟 ALL 150 TOOLS PASSED WITH 100% SUCCESS RATE! 🌟\n")
        return True

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
