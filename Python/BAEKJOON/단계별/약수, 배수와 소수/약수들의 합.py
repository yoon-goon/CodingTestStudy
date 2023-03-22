# https://www.acmicpc.net/problem/9506
import sys

N = 0

while N != -1:
    N = int(sys.stdin.readline())
    A = []

    for i in range(1, N + 1):
        if N % i == 0:
            A.append(i)

    if sum(A[:-1]) == N:
        print(N, "=", end=' ')
        for y in A:
            print(y, "+", end=' ')

    else:
        print(N, "is NOT perfect.")
