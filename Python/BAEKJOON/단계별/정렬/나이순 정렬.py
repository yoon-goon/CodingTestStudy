# https://www.acmicpc.net/problem/10814
import sys

n = int(input())
lst = []

for i in range(n):
    x, y = sys.stdin.readline().strip().split()
    lst.append([x, y])


for i in lst:
    print(*i)
