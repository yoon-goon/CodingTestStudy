# https://www.acmicpc.net/problem/2738
import sys

N, M = map(int,input().split())
A = []
B = []

for _ in range(M):
    A.append(sys.stdin.readline().rstrip())

for _ in range(M):
    B.append(sys.stdin.readline().rstrip())
print(A + B)
