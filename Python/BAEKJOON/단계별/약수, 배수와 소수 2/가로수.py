# https://www.acmicpc.net/problem/2485
import sys

n = int(sys.stdin.readline())
lst = []
a = int(sys.stdin.readline())
for _ in range(n-1):
    b = int(sys.stdin.readline())
    lst.append(b-a)
    a = b

print(lst)