# https://www.acmicpc.net/problem/11651
import sys

n = int(input())
lst = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    lst.append([y, x])

print(lst)
