# https://www.acmicpc.net/problem/11653

N = int(input())

if N == 1:
    pass
else:
    while True:
        for i in range(2,N+1):
            if N % i == 0:
                print(i)
                N %= 1
