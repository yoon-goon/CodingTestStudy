# https://www.acmicpc.net/problem/10798
import sys

A = []

for _ in range(5):
    A.append(sys.stdin.readline().split())

print(A)

for i in range(15):
    for y in range(5):
        try:
            print(A[i][y], end='')
        except:
            print('', end='')
