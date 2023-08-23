# https://www.acmicpc.net/problem/11651
import sys

n = int(input())
lst = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    lst.append([y, x])

lst.sort()

for i in range(n):
    lst[i][0], lst[i][1] = lst[i][1], lst[i][0]


print(''.join(lst))