# https://www.acmicpc.net/problem/2775
import sys

t = int(input())

for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    #  0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다
    lst = [i for i in range(1, n + 1)] # 1,2,3,4 ...
    # print(lst)
    for y in range(k):
        for j in range(1,n): # 1층 1호면 1명, 1층 2호면 1+2, 1층 3호면 1+2+3
            lst[j] += lst[j-1]

    print(lst)