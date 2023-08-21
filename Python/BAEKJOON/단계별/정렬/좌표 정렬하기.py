# https://www.acmicpc.net/problem/11650
import sys

n = int(input())
xlst = []
ylst = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    xlst.append(x)
    ylst.append(y)

print(xlst,ylst)