# https://www.acmicpc.net/problem/10798
import sys

A = []

for _ in range(5):
    A.append(sys.stdin.readline().rstrip())

for i in range(15):
    for y in range(5):
        try:
            print(A[y][i], end='')
        except IndexError:
            print('', end='')
