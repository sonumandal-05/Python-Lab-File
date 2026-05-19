import time
import sys

animation = ["[■□□□□□□□□□]",
             "[■■□□□□□□□□]",
             "[■■■□□□□□□□]",
             "[■■■■□□□□□□]",
             "[■■■■■□□□□□]",
             "[■■■■■■□□□□]",
             "[■■■■■■■□□□]",
             "[■■■■■■■■□□]",
             "[■■■■■■■■■□]",
             "[■■■■■■■■■■]"]

for i in range(3):
    for frame in animation:
        sys.stdout.write("\rLoading " + frame)
        sys.stdout.flush()
        time.sleep(0.2)

print("\nSystem Hacked Successfully 😈")