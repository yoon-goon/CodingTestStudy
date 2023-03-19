# https://www.acmicpc.net/problem/5086
import sys

A, B = 1, 1
while (A, B) == (0, 0):
    A, B = map(int, sys.stdin.readline().split())
    if B % A == 0:
        print('factor')
    elif A % B == 0:
        print('multiple')
    else:
        print('neither')
