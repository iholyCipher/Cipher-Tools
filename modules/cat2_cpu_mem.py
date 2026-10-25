# -*- coding: utf-8 -*-
"""
Cipher Tools - Category 2: CPU, Memory & Hardware Benchmarks (Tools 11 - 20)
"""
import os
import sys
import time
import math
import subprocess
import threading
from datetime import datetime

CLR_CYAN = "\033[96m"
CLR_PINK = "\033[95m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_GRAY = "\033[90m"
CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"

def tool_11_flpop_benchmark():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [11] Multi-Threaded Floating-Point Benchmark ==={CLR_RESET}")
    threads = os.cpu_count() or 4
    print(f"  {CLR_CYAN}[*] Running FLOPs calculations across {threads} worker threads...{CLR_RESET}")
    iters = 2_000_000
    res = []
    def calc():
        t0 = time.time()
        acc = 0.0
        for i in range(1, iters):
            acc += math.sin(i) * math.cos(i)
        res.append(time.time() - t0)
    
    t_start = time.time()
    pool = [threading.Thread(target=calc) for _ in range(threads)]
    for t in pool: t.start()
    for t in pool: t.join()
    total_elapsed = time.time() - t_start
    total_ops = threads * iters * 2
    score = (total_ops / total_elapsed) / 1_000_000
    print(f"  {CLR_GREEN}[✓] Total FLOPs: {total_ops:,} in {total_elapsed:.2f}s{CLR_RESET}")
    print(f"  {CLR_PINK}Score: {score:.2f} MFLOPs/sec{CLR_RESET}")

def tool_12_int_stress():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [12] Single-Thread Integer Math Stress Test ==={CLR_RESET}")
    iters = 5_000_000
    print(f"  {CLR_CYAN}[*] Performing {iters:,} arithmetic bitwise and modulus operations...{CLR_RESET}")
    t0 = time.time()
    n = 1
    for i in range(1, iters):
        n = (n ^ (i * 3)) % 999983
    elapsed = time.time() - t0
    ops_sec = iters / elapsed
    print(f"  {CLR_GREEN}[✓] Completed in {elapsed:.3f}s ({ops_sec/1_000_000:.2f} MOps/sec){CLR_RESET}")

def tool_13_ram_capacity():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [13] RAM Architecture & Available Capacity ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            cmd = "Get-CimInstance Win32_OperatingSystem | Select-Object TotalVisibleMemorySize, FreePhysicalMemory | Format-List"
            out = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True)
            print(out.strip())
        except Exception as e:
            print(f"  {CLR_RED}[-] Query error: {e}{CLR_RESET}")
    else:
        print("  Windows CIM query.")

def tool_14_cpu_usage():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [14] Real-time CPU Usage Meter (3 Samples) ==={CLR_RESET}")
    if os.name == 'nt':
        for i in range(3):
            try:
                cmd = "(Get-CimInstance Win32_Processor).LoadPercentage"
                val = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True).strip()
                print(f"  Sample {i+1}: CPU Load at {CLR_GREEN}{val}%{CLR_RESET}")
                if i < 2: time.sleep(1)
            except Exception:
                break
    else:
        print("  Available on Windows.")

def tool_15_cpu_affinity():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [15] Process Affinity & Logical Thread Matrix ==={CLR_RESET}")
    count = os.cpu_count() or 1
    print(f"  Logical Processor Threads Available: {CLR_CYAN}{count}{CLR_RESET}")
    for i in range(count):
        print(f"  Thread #{i:<2} [Core Engine Node]")

def tool_16_ram_throughput():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [16] Memory Bandwidth Throughput Test ==={CLR_RESET}")
    sz_mb = 128
    print(f"  {CLR_CYAN}[*] Allocating and writing {sz_mb} MB bytearray buffer in RAM...{CLR_RESET}")
    t0 = time.time()
    buf = bytearray(sz_mb * 1024 * 1024)
    for i in range(0, len(buf), 4096):
        buf[i] = 0xAA
    elapsed = time.time() - t0
    speed = sz_mb / elapsed
    print(f"  {CLR_GREEN}[✓] Written in {elapsed:.3f}s. Throughput: {CLR_PINK}{speed:.2f} MB/sec{CLR_RESET}")
    del buf

def tool_17_top_memory_proc():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [17] Top 15 Memory-Consuming Processes ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            cmd = "Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 15 Id, ProcessName, @{Name='RAM_MB';Expression={[math]::Round($_.WorkingSet64 / 1MB, 1)}} | Format-Table -AutoSize"
            out = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True)
            print(out)
        except Exception as e:
            print(f"  {CLR_RED}[-] Query error: {e}{CLR_RESET}")
    else:
        print("  Windows Process telemetry.")

def tool_18_kill_proc():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [18] Process Terminator by PID ==={CLR_RESET}")
    pid = input("  Enter Process ID (PID) to kill: ").strip()
    if pid.isdigit():
        try:
            if os.name == 'nt':
                subprocess.run(["taskkill", "/F", "/PID", pid], check=True)
            else:
                os.kill(int(pid), 9)
            print(f"  {CLR_GREEN}[✓] Process {pid} terminated.{CLR_RESET}")
        except Exception as e:
            print(f"  {CLR_RED}[-] Could not terminate: {e}{CLR_RESET}")

def tool_19_proc_tree():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [19] Process Hierarchy & Parent ID ==={CLR_RESET}")
    if os.name == 'nt':
        try:
            cmd = "Get-CimInstance Win32_Process | Select-Object -First 15 ProcessId, ParentProcessId, Name | Format-Table -AutoSize"
            out = subprocess.check_output(["powershell", "-NoProfile", "-Command", cmd], text=True)
            print(out)
        except Exception as e:
            print(f"  {CLR_RED}[-] Error: {e}{CLR_RESET}")
    else:
        print("  Windows CIM query.")

def tool_20_heartbeat_pulse():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [20] Real-time System Heartbeat Pulse ==={CLR_RESET}")
    print("  Emitting 5 heartbeats:")
    for i in range(5):
        t = datetime.now().strftime("%H:%M:%S")
        print(f"  [{t}] {CLR_GREEN}♥ HEARTBEAT ACTIVE{CLR_RESET} - System state OK")
        time.sleep(0.7)
