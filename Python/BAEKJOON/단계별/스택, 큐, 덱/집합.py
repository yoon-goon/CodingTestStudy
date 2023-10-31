# https://www.acmicpc.net/problem/11723
import sys

m = int(input())
s = set()

for _ in range(m):
    a = list(sys.stdin.readline().split())
    if a[0] == 'add':
        s.add(a[1])
    elif a[0] == 'remove':
        if a[1] in s:
            s.remove(a[1])
    elif a[0] == 'check':
        if a[1] in s:
            print(1)
        else:
            print(0)
    elif a[0] == 'toggle':
        if a[1] in s:
            s.remove(a[1])
        else:
            s.add(a[1])
    elif a[0] == 'all':
        s = set(range(1,21))
