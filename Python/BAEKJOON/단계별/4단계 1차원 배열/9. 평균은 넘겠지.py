# https://www.acmicpc.net/problem/4344
import sys

cases = int(input())

for i in range(cases):
    A = list(map(int, sys.stdin.readline().split()))
    avg = sum(A[1:]) / A[0]
    cnt = 0
    for y in range(1, len(A)):
        if A[y] > avg:
            cnt += 1

    print(f"{cnt / (len(A) - 1) * 100:.3f}%")
