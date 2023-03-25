# https://www.acmicpc.net/problem/11653

N = int(input())
i = 2

if N == 1:
    pass
else:
    # for i in range(2, N):
    while N >= 2:
        if N % i == 0:
            print(i)
            N = N / i
            i = 2
        else:
            i += 1
