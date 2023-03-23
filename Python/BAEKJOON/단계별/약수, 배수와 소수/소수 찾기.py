# https://www.acmicpc.net/problem/1978
import sys

Nums = int(input())

A = sys.stdin.readline().split()

print(A)
for i in A:
    B = []
    if i == 1:
        pass
    else:
        for y in range(1,i):
            if i % y == 0:
                B.append(y)
