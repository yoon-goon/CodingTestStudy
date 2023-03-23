# https://www.acmicpc.net/problem/1978
import sys

cnt = 0
Nums = int(input())

A = sys.stdin.readline().split()

print(A)
for i in A:
    B = []
    if i == 1:
        pass
    else:
        for y in range(1, i):
            if i % y == 0:
                B.append(y)
            if len(B) == 2:
                cnt += 1

print(cnt)