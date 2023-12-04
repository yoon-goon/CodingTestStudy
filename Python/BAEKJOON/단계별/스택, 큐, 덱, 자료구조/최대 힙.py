# https://www.acmicpc.net/problem/11279
import sys
import heapq

n = int(input())
hp = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x:  # 0이 아닐때
        heapq.heappush(hp, (-x, x)) # 튜플(tuple)를 원소로 추가하거나 삭제하면,
                                    # 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리
    else:
        if len(hp) >= 1:
            print(heapq.heappop(hp)[1])
        else:
            print(0)

# 참조 https://www.daleseo.com/python-heapq/ - 파이썬 heapq 모듈
