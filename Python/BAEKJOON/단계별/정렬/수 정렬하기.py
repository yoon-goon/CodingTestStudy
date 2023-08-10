# https://www.acmicpc.net/problem/2750
import sys

n = int(input())
lst = []

for _ in range(n):
    lst.append(int(sys.stdin.readline().strip()))

print(sorted(lst))
