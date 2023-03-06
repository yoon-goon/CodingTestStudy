# https://www.acmicpc.net/problem/2738
import sys

N, M = map(int, input().split())
A = []
B = []

for _ in range(M):
    A.append(sys.stdin.readline().rstrip().split())

for _ in range(M):
    B.append(sys.stdin.readline().rstrip().split())

for i in range(N):
    for y in range(M):
        print(int(A[i][y]) + int(B[i][y]), end=' ')
    print('')
