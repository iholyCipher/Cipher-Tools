# -*- coding: utf-8 -*-
"""
Cipher Tools - Category 12: Advanced Data Science, Mathematical & Statistical Engines (Tools 151 - 200)
Zero external dependencies. Pure standard library.
"""
import math
import statistics
import random

CLR_CYAN = "\033[96m"
CLR_PINK = "\033[95m"
CLR_GREEN = "\033[92m"
CLR_YELLOW = "\033[93m"
CLR_RED = "\033[91m"
CLR_GRAY = "\033[90m"
CLR_RESET = "\033[0m"
CLR_BOLD = "\033[1m"

def _parse_floats(prompt, default="10, 20, 30, 40, 50"):
    raw = input(f"  {prompt} [default '{default}']: ").strip() or default
    return [float(x.strip()) for x in raw.replace(",", " ").split() if x.strip()]

def tool_151_mean_median_mode():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [151] Mean, Median & Mode Calculator ==={CLR_RESET}")
    nums = _parse_floats("Enter numbers separated by comma/space")
    print(f"  Sample Count: {len(nums)}")
    print(f"  Mean        : {CLR_GREEN}{statistics.mean(nums):.4f}{CLR_RESET}")
    print(f"  Median      : {CLR_GREEN}{statistics.median(nums):.4f}{CLR_RESET}")
    try:
        print(f"  Mode        : {CLR_GREEN}{statistics.mode(nums):.4f}{CLR_RESET}")
    except Exception:
        print(f"  Mode        : {CLR_GRAY}No unique mode{CLR_RESET}")

def tool_152_std_dev_variance():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [152] Standard Deviation & Variance ==={CLR_RESET}")
    nums = _parse_floats("Enter dataset")
    if len(nums) < 2:
        print(f"  {CLR_RED}[-] At least 2 values required.{CLR_RESET}")
        return
    print(f"  Variance (Sample) : {CLR_GREEN}{statistics.variance(nums):.4f}{CLR_RESET}")
    print(f"  Std Deviation (S) : {CLR_GREEN}{statistics.stdev(nums):.4f}{CLR_RESET}")
    print(f"  Std Deviation (Pop): {CLR_CYAN}{statistics.pstdev(nums):.4f}{CLR_RESET}")

def tool_153_min_max_range():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [153] Min, Max & Dynamic Range ==={CLR_RESET}")
    nums = _parse_floats("Enter dataset")
    mn, mx = min(nums), max(nums)
    print(f"  Minimum : {CLR_CYAN}{mn}{CLR_RESET}")
    print(f"  Maximum : {CLR_CYAN}{mx}{CLR_RESET}")
    print(f"  Range   : {CLR_GREEN}{mx - mn}{CLR_RESET}")
    print(f"  Sum     : {sum(nums):.4f}")

def tool_154_percentiles():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [154] Percentile & Quartile Calculator (P25, P50, P75, P90, P99) ==={CLR_RESET}")
    nums = sorted(_parse_floats("Enter dataset", "12, 15, 23, 29, 35, 42, 55, 67, 89, 99"))
    def pct(p):
        k = (len(nums) - 1) * (p / 100.0)
        f = math.floor(k); c = math.ceil(k)
        if f == c: return nums[int(k)]
        return nums[f] * (c - k) + nums[c] * (k - f)
    print(f"  Q1 (P25) : {pct(25):.2f}")
    print(f"  Median   : {pct(50):.2f}")
    print(f"  Q3 (P75) : {pct(75):.2f}")
    print(f"  P90      : {pct(90):.2f}")
    print(f"  P99      : {pct(99):.2f}")

def tool_155_distribution_histogram():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [155] ASCII Number Distribution Histogram ==={CLR_RESET}")
    nums = _parse_floats("Enter dataset", "5, 12, 14, 22, 25, 28, 31, 33, 45, 48, 50")
    mn, mx = min(nums), max(nums)
    bins = 5
    span = (mx - mn) / bins if mx > mn else 1
    counts = [0] * bins
    for n in nums:
        idx = min(int((n - mn) / span), bins - 1)
        counts[idx] += 1
    for i in range(bins):
        low, high = mn + i * span, mn + (i + 1) * span
        bar = "█" * (counts[i] * 3)
        print(f"  [{low:5.1f} - {high:5.1f}]: {CLR_PINK}{bar:<20}{CLR_RESET} ({counts[i]})")

def tool_156_z_score_normalizer():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [156] Z-Score Statistical Normalizer ==={CLR_RESET}")
    nums = _parse_floats("Enter dataset", "10, 20, 30, 40, 50")
    if len(nums) < 2: return
    m, s = statistics.mean(nums), statistics.stdev(nums)
    z_scores = [(x - m) / s for x in nums]
    print(f"  Mean: {m:.2f}, Stdev: {s:.2f}")
    for orig, z in zip(nums[:8], z_scores[:8]):
        print(f"  Value: {orig:<8} -> Z-Score: {CLR_GREEN}{z:+.3f}{CLR_RESET}")

def tool_157_min_max_scaler():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [157] Feature Min-Max Scaler [0.0 - 1.0] ==={CLR_RESET}")
    nums = _parse_floats("Enter values", "10, 25, 50, 75, 100")
    mn, mx = min(nums), max(nums)
    diff = mx - mn if mx != mn else 1.0
    scaled = [(x - mn) / diff for x in nums]
    for orig, sc in zip(nums[:8], scaled[:8]):
        print(f"  {orig:<8} -> {CLR_CYAN}{sc:.4f}{CLR_RESET}")

def tool_158_pearson_correlation():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [158] Pearson Correlation Coefficient ==={CLR_RESET}")
    x = _parse_floats("Enter X array", "1, 2, 3, 4, 5")
    y = _parse_floats("Enter Y array", "2, 4, 6, 8, 10")
    if len(x) != len(y) or len(x) < 2:
        print(f"  {CLR_RED}[-] Datasets must have identical length >= 2.{CLR_RESET}")
        return
    mx, my = statistics.mean(x), statistics.mean(y)
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    den = math.sqrt(sum((a - mx)**2 for a in x) * sum((b - my)**2 for b in y))
    r = num / den if den else 0
    print(f"  Pearson Correlation r: {CLR_GREEN}{r:.4f}{CLR_RESET}")

def tool_159_linear_regression():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [159] Simple Linear Regression (Slope & Intercept) ==={CLR_RESET}")
    x = _parse_floats("Enter X values", "1, 2, 3, 4, 5")
    y = _parse_floats("Enter Y values", "3, 5, 7, 9, 11")
    if len(x) != len(y) or len(x) < 2: return
    n = len(x)
    sx, sy = sum(x), sum(y)
    sxy = sum(a * b for a, b in zip(x, y))
    sx2 = sum(a * a for a in x)
    slope = (n * sxy - sx * sy) / (n * sx2 - sx * sx)
    intercept = (sy - slope * sx) / n
    print(f"  Model Equation: {CLR_GREEN}y = {slope:.4f}x + {intercept:.4f}{CLR_RESET}")

def tool_160_moving_average():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [160] Simple Moving Average (SMA) Generator ==={CLR_RESET}")
    nums = _parse_floats("Enter time series", "10, 12, 15, 14, 18, 20, 22, 21")
    w = int(input("  Enter window size (default 3): ").strip() or "3")
    sma = []
    for i in range(len(nums) - w + 1):
        sma.append(sum(nums[i:i+w]) / w)
    print(f"  SMA Window {w}: {[round(x, 2) for x in sma]}")

def tool_161_prime_checker():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [161] Deterministic Prime Number Validator ==={CLR_RESET}")
    n = int(input("  Enter integer to test: ").strip() or "999983")
    if n < 2: is_p = False
    elif n in (2, 3): is_p = True
    elif n % 2 == 0 or n % 3 == 0: is_p = False
    else:
        is_p = True
        for i in range(5, int(math.isqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                is_p = False; break
    status = f"{CLR_GREEN}PRIME{CLR_RESET}" if is_p else f"{CLR_RED}COMPOSITE{CLR_RESET}"
    print(f"  Number {n:,} is {status}")

def tool_162_prime_sieve():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [162] Sieve of Eratosthenes (Primes up to N) ==={CLR_RESET}")
    lim = min(int(input("  Enter upper limit (max 100,000, default 100): ").strip() or "100"), 100_000)
    sieve = [True] * (lim + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(math.isqrt(lim)) + 1):
        if sieve[p]:
            for i in range(p * p, lim + 1, p):
                sieve[i] = False
    primes = [i for i, is_p in enumerate(sieve) if is_p]
    print(f"  Found {len(primes)} primes up to {lim}:")
    print(f"  {primes[:20]}{' ...' if len(primes) > 20 else ''}")

def tool_163_gcd_lcm():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [163] Greatest Common Divisor (GCD) & LCM ==={CLR_RESET}")
    a = int(input("  Enter number A: ").strip() or "48")
    b = int(input("  Enter number B: ").strip() or "18")
    g = math.gcd(a, b)
    lcm = abs(a * b) // g if g else 0
    print(f"  GCD({a}, {b}) = {CLR_GREEN}{g}{CLR_RESET}")
    print(f"  LCM({a}, {b}) = {CLR_GREEN}{lcm}{CLR_RESET}")

def tool_164_modular_inverse():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [164] Modular Multiplicative Inverse (RSA Math) ==={CLR_RESET}")
    a = int(input("  Enter base integer a: ").strip() or "3")
    m = int(input("  Enter modulus m: ").strip() or "11")
    try:
        inv = pow(a, -1, m)
        print(f"  Inverse: ({a}^-1) mod {m} = {CLR_GREEN}{inv}{CLR_RESET}")
    except ValueError:
        print(f"  {CLR_RED}[-] Inverse does not exist (GCD != 1).{CLR_RESET}")

def tool_165_combinations_permutations():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [165] Combinations (nCr) & Permutations (nPr) ==={CLR_RESET}")
    n = int(input("  Enter n (total items): ").strip() or "10")
    r = int(input("  Enter r (subset items): ").strip() or "3")
    ncr = math.comb(n, r) if hasattr(math, 'comb') else math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    npr = math.perm(n, r) if hasattr(math, 'perm') else math.factorial(n) // math.factorial(n - r)
    print(f"  nCr ({n} choose {r}): {CLR_GREEN}{ncr:,}{CLR_RESET}")
    print(f"  nPr ({n} permute {r}): {CLR_CYAN}{npr:,}{CLR_RESET}")

def tool_166_arbitrary_factorial():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [166] Arbitrary-Precision Factorial (N!) ==={CLR_RESET}")
    n = int(input("  Enter integer n (default 25): ").strip() or "25")
    f = math.factorial(n)
    s = str(f)
    print(f"  {n}! = {CLR_GREEN}{s if len(s) < 80 else s[:75] + '...'}{CLR_RESET}")
    print(f"  Digit Count: {len(s)}")

def tool_167_fibonacci_series():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [167] Fibonacci Generator (First N Terms) ==={CLR_RESET}")
    n = min(int(input("  Enter count of terms (default 15): ").strip() or "15"), 500)
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    print(f"  Fibonacci({n}): {seq[:n]}")

def tool_168_quadratic_solver():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [168] Quadratic Equation Solver (ax² + bx + c = 0) ==={CLR_RESET}")
    a = float(input("  Enter coefficient a: ").strip() or "1")
    b = float(input("  Enter coefficient b: ").strip() or "-5")
    c = float(input("  Enter coefficient c: ").strip() or "6")
    d = b * b - 4 * a * c
    print(f"  Discriminant Δ = {d}")
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"  Roots: x1 = {CLR_GREEN}{x1}{CLR_RESET}, x2 = {CLR_GREEN}{x2}{CLR_RESET}")
    elif d == 0:
        print(f"  Double Root: x = {CLR_GREEN}{-b / (2 * a)}{CLR_RESET}")
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-d) / (2 * a)
        print(f"  Complex Roots: {real:.2f} ± {imag:.2f}i")

def tool_169_matrix_determinant_2x2_3x3():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [169] Matrix Determinant (2x2 & 3x3) ==={CLR_RESET}")
    print("  3x3 Matrix Determinant sample [[1,2,3],[0,1,4],[5,6,0]]:")
    mat = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
    det = (mat[0][0]*(mat[1][1]*mat[2][2] - mat[1][2]*mat[2][1]) -
           mat[0][1]*(mat[1][0]*mat[2][2] - mat[1][2]*mat[2][0]) +
           mat[0][2]*(mat[1][0]*mat[2][1] - mat[1][1]*mat[2][0]))
    print(f"  det(A) = {CLR_GREEN}{det}{CLR_RESET}")

def tool_170_vector_dot_cross_product():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [170] Vector Dot & Cross Product (3D) ==={CLR_RESET}")
    v1 = _parse_floats("Vector 1 (x,y,z)", "1, 2, 3")
    v2 = _parse_floats("Vector 2 (x,y,z)", "4, 5, 6")
    dot = sum(a * b for a, b in zip(v1[:3], v2[:3]))
    cross = [
        v1[1]*v2[2] - v1[2]*v2[1],
        v1[2]*v2[0] - v1[0]*v2[2],
        v1[0]*v2[1] - v1[1]*v2[0]
    ]
    print(f"  Dot Product (Scalar) : {CLR_GREEN}{dot}{CLR_RESET}")
    print(f"  Cross Product (Vector): {CLR_CYAN}{cross}{CLR_RESET}")

def tool_171_euclidean_distance():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [171] N-Dimensional Euclidean Distance ==={CLR_RESET}")
    p1 = _parse_floats("Point A coordinates", "0, 0, 0")
    p2 = _parse_floats("Point B coordinates", "3, 4, 0")
    dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))
    print(f"  Euclidean Distance: {CLR_GREEN}{dist:.4f}{CLR_RESET}")

def tool_172_cosine_similarity():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [172] Vector Cosine Similarity (NLP & AI Math) ==={CLR_RESET}")
    v1 = _parse_floats("Vector A", "1, 2, 3")
    v2 = _parse_floats("Vector B", "2, 4, 5")
    dot = sum(a * b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(a*a for a in v1))
    mag2 = math.sqrt(sum(b*b for b in v2))
    cos_sim = dot / (mag1 * mag2) if (mag1 * mag2) else 0.0
    print(f"  Cosine Similarity: {CLR_GREEN}{cos_sim:.5f}{CLR_RESET}")

def tool_173_unit_converter_length():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [173] Length & Distance Unit Converter ==={CLR_RESET}")
    m = float(input("  Enter meters (default 100): ").strip() or "100")
    print(f"  Kilometers : {m / 1000:.4f} km")
    print(f"  Centimeters: {m * 100:.1f} cm")
    print(f"  Feet       : {m * 3.28084:.2f} ft")
    print(f"  Inches     : {m * 39.3701:.2f} in")
    print(f"  Miles      : {m / 1609.344:.5f} mi")

def tool_174_unit_converter_temperature():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [174] Temperature Converter (C / F / K) ==={CLR_RESET}")
    c = float(input("  Enter Celsius value (default 25): ").strip() or "25")
    f = (c * 9/5) + 32
    k = c + 273.15
    print(f"  Fahrenheit: {CLR_GREEN}{f:.2f} °F{CLR_RESET}")
    print(f"  Kelvin    : {CLR_CYAN}{k:.2f} K{CLR_RESET}")

def tool_175_unit_converter_data_storage():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [175] Data Storage Unit Interconverter (B / KB / MB / GB / TB) ==={CLR_RESET}")
    mb = float(input("  Enter Megabytes (default 1024): ").strip() or "1024")
    b = mb * (1024**2)
    print(f"  Bytes     : {int(b):,} B")
    print(f"  Kilobytes : {b / 1024:,.2f} KB")
    print(f"  Gigabytes : {mb / 1024:.4f} GB")
    print(f"  Terabytes : {mb / (1024**2):.6f} TB")

def tool_176_data_transfer_time():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [176] Network Download / Transfer Time Estimator ==={CLR_RESET}")
    sz_gb = float(input("  Enter file size in GB (default 10): ").strip() or "10")
    speed_mbps = float(input("  Enter bandwidth in Mbps (default 50): ").strip() or "50")
    sz_bits = sz_gb * 8 * 1024 * 1024 * 1024
    speed_bps = speed_mbps * 1000 * 1000
    sec = sz_bits / speed_bps if speed_bps else 0
    hrs = sec // 3600
    mins = (sec % 3600) // 60
    rem_s = sec % 60
    print(f"  Estimated Time: {CLR_GREEN}{int(hrs)}h {int(mins)}m {int(rem_s)}s ({sec:.1f} total sec){CLR_RESET}")

def tool_177_log_calculator():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [177] Logarithm Multi-Base Engine (ln, log2, log10) ==={CLR_RESET}")
    x = float(input("  Enter positive number x (default 1024): ").strip() or "1024")
    if x <= 0: return
    print(f"  log2({x})  : {CLR_GREEN}{math.log2(x):.4f}{CLR_RESET}")
    print(f"  log10({x}) : {CLR_CYAN}{math.log10(x):.4f}{CLR_RESET}")
    print(f"  ln({x})    : {math.log(x):.4f}")

def tool_178_outlier_detector_iqr():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [178] Statistical Outlier Detection (Tukey's IQR Method) ==={CLR_RESET}")
    nums = sorted(_parse_floats("Enter dataset", "10, 12, 14, 15, 16, 18, 19, 21, 22, 95"))
    n = len(nums)
    q1 = nums[int(n * 0.25)]
    q3 = nums[int(n * 0.75)]
    iqr = q3 - q1
    low = q1 - 1.5 * iqr
    high = q3 + 1.5 * iqr
    outliers = [x for x in nums if x < low or x > high]
    print(f"  Q1: {q1}, Q3: {q3}, IQR: {iqr}")
    print(f"  Bounds: [{low:.2f}, {high:.2f}]")
    print(f"  Detected Outliers: {CLR_RED}{outliers}{CLR_RESET}")

def tool_179_random_normal_distribution():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [179] Gaussian Normal Distribution Sampler (Box-Muller) ==={CLR_RESET}")
    samples = [random.gauss(0, 1) for _ in range(10)]
    print("  10 Random samples from N(0, 1):")
    for s in samples:
        print(f"  {s:+.4f}")

def tool_180_math_summary():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [180] Mathematical Constants & Machine Epsilon ==={CLR_RESET}")
    print(f"  π (pi)           : {math.pi}")
    print(f"  e (Euler)        : {math.e}")
    print(f"  τ (tau)          : {math.tau}")
    print(f"  Golden Ratio (φ) : {(1 + math.sqrt(5)) / 2}")
    import sys
    print(f"  Float Epsilon    : {sys.float_info.epsilon}")

def tool_181_harmonic_mean():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [181] Harmonic & Geometric Mean ==={CLR_RESET}")
    nums = _parse_floats("Enter positive values", "2, 4, 8")
    hm = statistics.harmonic_mean(nums)
    gm = statistics.geometric_mean(nums) if hasattr(statistics, 'geometric_mean') else math.prod(nums)**(1/len(nums))
    print(f"  Harmonic Mean : {CLR_GREEN}{hm:.4f}{CLR_RESET}")
    print(f"  Geometric Mean: {CLR_CYAN}{gm:.4f}{CLR_RESET}")

def tool_182_matrix_transpose():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [182] Matrix Transposition Engine ==={CLR_RESET}")
    m = [[1, 2, 3], [4, 5, 6]]
    t = [list(row) for row in zip(*m)]
    print("  Original Matrix:")
    for r in m: print(f"    {r}")
    print("  Transposed Matrix:")
    for r in t: print(f"    {CLR_GREEN}{r}{CLR_RESET}")

def tool_183_matrix_multiplication():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [183] 2D Matrix Multiplication ==={CLR_RESET}")
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    res = [[sum(x*y for x, y in zip(row_a, col_b)) for col_b in zip(*b)] for row_a in a]
    print(f"  Matrix A x B = {CLR_GREEN}{res}{CLR_RESET}")

def tool_184_angle_converter():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [184] Radians & Degrees Converter ==={CLR_RESET}")
    deg = float(input("  Enter degrees (default 180): ").strip() or "180")
    rad = math.radians(deg)
    print(f"  Radians: {CLR_GREEN}{rad:.6f}{CLR_RESET} (or {rad/math.pi:.2f}π)")

def tool_185_bitwise_truth_table():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [185] Logic Gates Truth Table (AND, OR, XOR, NAND) ==={CLR_RESET}")
    print("  A | B | AND | OR | XOR | NAND")
    print("  -----------------------------")
    for a in (0, 1):
        for b in (0, 1):
            print(f"  {a} | {b} |  {a&b}  | {a|b}  |  {a^b}  |  {int(not(a&b))}")

def tool_186_base_expansion():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [186] Floating Point to IEEE-754 Hex & Binary ==={CLR_RESET}")
    val = float(input("  Enter float value (default 3.14159): ").strip() or "3.14159")
    import struct
    b = struct.pack('>f', val)
    hx = b.hex().upper()
    print(f"  IEEE-754 32-bit Single Precision Hex: {CLR_GREEN}0x{hx}{CLR_RESET}")
    print(f"  Binary: {' '.join(f'{byte:08b}' for byte in b)}")

def tool_187_entropy_calculator_series():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [187] Discrete Shannon Information Entropy ==={CLR_RESET}")
    s = input("  Enter string to calculate entropy: ").strip() or "cipher_tools_titan_suite"
    counts = {c: s.count(c) for c in set(s)}
    l = len(s)
    ent = -sum((cnt/l) * math.log2(cnt/l) for cnt in counts.values())
    print(f"  Information Entropy: {CLR_GREEN}{ent:.4f} bits/symbol{CLR_RESET}")

def tool_188_speed_converter():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [188] Speed & Velocity Converter (km/h, mph, m/s, knots) ==={CLR_RESET}")
    kmh = float(input("  Enter km/h (default 100): ").strip() or "100")
    print(f"  Miles per hour (mph): {kmh * 0.621371:.2f}")
    print(f"  Meters/sec (m/s)    : {kmh / 3.6:.2f}")
    print(f"  Knots (nautical)    : {kmh * 0.539957:.2f}")

def tool_189_pressure_converter():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [189] Pressure Unit Converter (Bar, PSI, Pascal, atm) ==={CLR_RESET}")
    bar = float(input("  Enter Bar (default 1.0): ").strip() or "1.0")
    print(f"  Pascals (Pa)   : {bar * 100000:,.1f}")
    print(f"  PSI            : {bar * 14.5038:.2f}")
    print(f"  Standard Atm   : {bar * 0.986923:.4f}")

def tool_190_bmi_calculator():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [190] Body Mass Index (BMI) & Metabolic Metric ==={CLR_RESET}")
    kg = float(input("  Enter weight in kg (default 70): ").strip() or "70")
    cm = float(input("  Enter height in cm (default 175): ").strip() or "175")
    m = cm / 100
    bmi = kg / (m * m) if m else 0
    print(f"  BMI Score: {CLR_GREEN}{bmi:.1f}{CLR_RESET}")
    if bmi < 18.5: print("  Category : Underweight")
    elif bmi < 25: print("  Category : Normal weight")
    elif bmi < 30: print("  Category : Overweight")
    else: print("  Category : Obese")

def tool_191_loan_mortgage():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [191] Amortization & Monthly Payment Formula ==={CLR_RESET}")
    principal = float(input("  Enter principal amount (default 10000): ").strip() or "10000")
    annual_rate = float(input("  Enter annual interest % (default 5): ").strip() or "5")
    months = int(input("  Enter term in months (default 36): ").strip() or "36")
    r = (annual_rate / 100) / 12
    if r == 0: pmt = principal / months
    else: pmt = (principal * r * (1 + r)**months) / ((1 + r)**months - 1)
    print(f"  Monthly Installment: {CLR_GREEN}{pmt:.2f}{CLR_RESET}")
    print(f"  Total Repayment    : {pmt * months:.2f}")

def tool_192_compound_interest():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [192] Compound Interest & Growth Projector ==={CLR_RESET}")
    p = float(input("  Principal (default 1000): ").strip() or "1000")
    r = float(input("  Annual Interest Rate % (default 7): ").strip() or "7") / 100
    t = float(input("  Years (default 10): ").strip() or "10")
    a = p * (1 + r)**t
    print(f"  Future Value: {CLR_GREEN}{a:.2f}{CLR_RESET} (+{a - p:.2f} interest)")

def tool_193_discount_tax():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [193] Discount, VAT & Sales Tax Engine ==={CLR_RESET}")
    price = float(input("  Enter initial price: ").strip() or "120")
    vat = float(input("  Enter VAT/Tax % (default 10): ").strip() or "10")
    final = price * (1 + vat / 100)
    print(f"  Tax Amount : {price * (vat / 100):.2f}")
    print(f"  Total Final: {CLR_GREEN}{final:.2f}{CLR_RESET}")

def tool_194_percentage_change():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [194] Percentage Difference & Relative Delta ==={CLR_RESET}")
    old = float(input("  Enter original value: ").strip() or "50")
    new = float(input("  Enter new value: ").strip() or "75")
    chg = ((new - old) / old) * 100 if old else 0
    print(f"  Change: {CLR_GREEN if chg >= 0 else CLR_RED}{chg:+.2f}%{CLR_RESET}")

def tool_195_energy_converter():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [195] Energy & Work Unit Converter (Joules, Calories, kWh) ==={CLR_RESET}")
    j = float(input("  Enter Joules (default 10000): ").strip() or "10000")
    print(f"  Kilojoules (kJ)    : {j / 1000:.3f}")
    print(f"  Kilocalories (kcal): {j / 4184:.3f}")
    print(f"  Kilowatt-hour (kWh): {j / 3600000:.6f}")

def tool_196_fuel_consumption():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [196] Fuel Consumption Converter (L/100km to MPG) ==={CLR_RESET}")
    l100 = float(input("  Enter Liters per 100km (default 7.5): ").strip() or "7.5")
    mpg = 235.215 / l100 if l100 else 0
    print(f"  US MPG: {CLR_GREEN}{mpg:.1f} mpg{CLR_RESET}")

def tool_197_time_dilation_simulator():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [197] Special Relativity Time Dilation Simulator ==={CLR_RESET}")
    c_ratio = float(input("  Enter velocity fraction of c (e.g. 0.9): ").strip() or "0.9")
    if 0 <= c_ratio < 1:
        gamma = 1 / math.sqrt(1 - c_ratio**2)
        print(f"  Lorentz Factor γ: {CLR_GREEN}{gamma:.4f}{CLR_RESET}")
        print(f"  1 hour on traveler ship = {gamma:.2f} hours for stationary observer")

def tool_198_sound_speed():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [198] Speed of Sound in Air by Temperature ==={CLR_RESET}")
    c = float(input("  Enter air temperature in °C (default 20): ").strip() or "20")
    v = 331.3 * math.sqrt(1 + c / 273.15)
    print(f"  Speed of Sound: {CLR_GREEN}{v:.2f} m/s{CLR_RESET} ({v * 3.6:.1f} km/h)")

def tool_199_trig_identities():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [199] Comprehensive Trigonometric Evaluator ==={CLR_RESET}")
    deg = float(input("  Enter angle in degrees: ").strip() or "45")
    rad = math.radians(deg)
    print(f"  sin({deg}°) = {math.sin(rad):.4f}")
    print(f"  cos({deg}°) = {math.cos(rad):.4f}")
    print(f"  tan({deg}°) = {math.tan(rad):.4f}")

def tool_200_math_benchmark_battery():
    print(f"\n {CLR_BOLD}{CLR_YELLOW}=== [200] Fast Mathematical Compute Stress Battery ==={CLR_RESET}")
    import time
    t0 = time.time()
    total = sum(math.isqrt(i) for i in range(1, 1_000_000))
    el = time.time() - t0
    print(f"  {CLR_GREEN}[✓] 1,000,000 integer square roots computed in {el:.3f}s{CLR_RESET}")
