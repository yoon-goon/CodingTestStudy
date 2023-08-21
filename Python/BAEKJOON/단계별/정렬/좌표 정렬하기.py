# https://www.acmicpc.net/problem/11650
import sys

n = int(input())
xlst = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    xlst.append([x, y])

print(sorted(xlst))
