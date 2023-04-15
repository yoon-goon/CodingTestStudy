# https://www.acmicpc.net/problem/11053
import sys

N = int(input())

A = list(map(int, sys.stdin.readline().split()))

cnt = 1

for i in range(1, len(A)):
    if A[i] > A[i - 1]:
        cnt += 1

print(cnt)
