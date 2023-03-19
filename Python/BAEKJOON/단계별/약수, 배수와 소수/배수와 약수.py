# https://www.acmicpc.net/problem/5086
import sys

A, B = 1, 1
while True:
    A, B = map(int, sys.stdin.readline().split())
    if (A, B) == (0, 0):
        break
    if B % A == 0:
        print('factor')
    elif A % B == 0:
        print('multiple')
    else:
        print('neither')
