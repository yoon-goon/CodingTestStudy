# https://www.acmicpc.net/problem/11279
import sys
import heapq

n = int(input())
hp = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(hp, (-x, x))
    else:
        if len(hp) >= 1:
            print(heapq.heappop(hp)[1])
        else:
            print(0)

# 참조 https://www.daleseo.com/python-heapq/ - 파이썬 heapq 모듈
