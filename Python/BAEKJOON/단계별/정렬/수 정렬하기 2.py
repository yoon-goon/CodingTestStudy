# https://www.acmicpc.net/problem/2751
import sys

n = int(input())

lst = []

for _ in range(n):
    lst.append(sys.stdin.readline().strip())

for i in range(n):
    print(sorted(lst)[i])
