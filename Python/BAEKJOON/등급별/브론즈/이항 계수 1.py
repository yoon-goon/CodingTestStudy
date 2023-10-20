# https://www.acmicpc.net/problem/11050
import sys


def facto(x):
    if x == 0:
        return 1
    else:
        return x * facto(x - 1)


n, k = map(int, sys.stdin.readline().split())

print(n, k)
