# https://www.acmicpc.net/problem/11723
import sys

m = int(input())
s = set()

for _ in range(m):
    a = list(sys.stdin.readline().split())
    if a[0] == 'add':
        s.append(a[1])
    elif a[0] == 'remove':
        if a[1] in s:
            s.remove(s[1])
