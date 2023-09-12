# https://www.acmicpc.net/problem/1735
import sys

a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())

upper = a1 * b2 + a2 * b1
lower = b1 * b2

print(upper, lower)
