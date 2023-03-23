# https://www.acmicpc.net/problem/1978
import sys

cnt = 0
Nums = int(input())

A = list(map(int, sys.stdin.readline().split()))

#print(A)
for i in A:
    B = []
    if i == 1:
        pass
    else:
        for y in range(1, i + 1):
            if i % y == 0:
                B.append(y)
                #print(B)
    if len(B) == 2:
        cnt += 1

print(cnt)
