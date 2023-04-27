# https://www.acmicpc.net/problem/11053
import sys

N = int(input())

A = list(map(int, sys.stdin.readline().split()))

cnt = 1

for i in range(1, len(A)):
    if A[i] > A[i - 1]:
        cnt += 1

print(cnt)

'''
반례
7
70 30 50 60 70 0 10
answer 4

8
10 50 60 70 20 30 40 50
answer 5
'''