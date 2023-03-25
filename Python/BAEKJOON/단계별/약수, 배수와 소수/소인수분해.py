# https://www.acmicpc.net/problem/11653

N = int(input())

if N == 1:
    pass
else:
    for i in range(2, N):
        if N % i == 0:
            print(i)
            N = N % i
