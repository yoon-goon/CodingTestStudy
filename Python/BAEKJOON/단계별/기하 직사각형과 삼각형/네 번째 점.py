# https://www.acmicpc.net/problem/3009

import sys

x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())
x3, y3 = map(int, sys.stdin.readline().split())

if x1 == x2:
    x = x3
elif x1 == x3:
    x = x2
elif x2 == x3:
    x = x1
if y1 == y2:
    y = y3
elif y1 == y3:
    y = y2
elif y2 == y3:
    y = y1

print(x, y)
