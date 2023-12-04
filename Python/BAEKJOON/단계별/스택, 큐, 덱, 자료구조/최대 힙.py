import sys
import heapq

n = int(input())
hp = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x == True:
        heapq.heappush(hp, (-x, x))
    else:
        if len(hp) >= 1:
            print(heapq.heappop(hp)[1])
        else:
            print(0)
