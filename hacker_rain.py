import random
import os
import time

char ="01ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=~`|\\:;\"'<>,.?/"

while True:
    line = "".join(random.choice(char) for _ in range(80))
    print("\033[92m" + line)
    time.sleep(0.05)
    