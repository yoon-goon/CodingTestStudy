# https://www.acmicpc.net/problem/4134
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a = int(sys.stdin.readline())
    b = 0
    while b == 0:
        for i in range(2, int(a ** 0.5) + 1):  # 루트
            if a % i == 0:
                a += 1
            else:
                print(a)
                b = 1
                break
