# https://www.acmicpc.net/problem/2798
import sys

N, M = map(int, input().split())
sums = []

print(N, M)

A = list(map(int, input().split()))

print(A)

for i in A:
    for j in (i + 1, A):
        for k in j + 1, A:
            print(i, j, k)
            if (i + j + k) <= M:
                sums.append(i + j + k)

print(max(sums))
