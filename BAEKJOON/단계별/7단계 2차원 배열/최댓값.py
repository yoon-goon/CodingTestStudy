# https://www.acmicpc.net/problem/2566
import sys

A = []
C = []
for i in range(9):
    B = sys.stdin.readline().split()
    C.append(max(B))
    A.append(B)

print(A)
print(max(C))
