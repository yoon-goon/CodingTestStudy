# https://www.acmicpc.net/problem/4134
import sys


def prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


n = int(sys.stdin.readline())

for _ in range(n):
    a = int(sys.stdin.readline())
