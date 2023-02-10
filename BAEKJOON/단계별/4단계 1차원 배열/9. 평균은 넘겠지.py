# https://www.acmicpc.net/problem/4344
import sys

cases = int(input())


for i in range(cases):
    A = list(map(int,sys.stdin.readline().split()))
    avg = sum(A[1:])/A[0]
    for y in range(1,len(A)):
        print(A[y])

    print(avg)