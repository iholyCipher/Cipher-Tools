import shutil
import random
import time
import os
import sys

def matrix_rain():
    os.system('cls' if os.name == 'nt' else 'clear')
    columns, rows = shutil.get_terminal_size(fallback=(80, 24))
    drops = [0] * columns
    chars = "0123456789ABCDEF!@#$%^&*()_+-=~[]{}|;:,.<>?/Antigravity"

    GREEN = "\033[92m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

    print("\033[?25l", end="") # Hide cursor
    try:
        while True:
            line = []
            for i in range(columns):
                if drops[i] == 0:
                    if random.random() < 0.04:
                        drops[i] = random.randint(5, rows)
                    line.append(" ")
                else:
                    char = random.choice(chars)
                    if random.random() < 0.2:
                        line.append(f"{WHITE}{char}{RESET}")
                    else:
                        line.append(f"{GREEN}{char}{RESET}")
                    drops[i] -= 1
            print("".join(line))
            time.sleep(0.04)
    except KeyboardInterrupt:
        print("\033[?25h" + RESET) # Show cursor
        print("\n[+] Antigravity Matrix Terminated safely.")

if __name__ == "__main__":
    matrix_rain()
