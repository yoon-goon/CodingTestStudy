# https://www.acmicpc.net/problem/2566
import sys

A = []
C = []
for _ in range(9):
    B = sys.stdin.readline().split()
    A.append(B)
    C.append(max(B))

print(C)

for i in range(9):
    for y in range(9):
        if A[i][y] == max(C):
            print(max(C))
            print(i + 1, y + 1)
