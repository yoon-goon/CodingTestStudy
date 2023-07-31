# https://www.acmicpc.net/problem/19532
import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())
brk = 0

for i in range(-999, 1000):
    for y in range(-999, 1000):
        if c == a * i + b * y and f == d * i + e * y:
            print(i, y)
            brk = 1
        if brk == 1:
            break
