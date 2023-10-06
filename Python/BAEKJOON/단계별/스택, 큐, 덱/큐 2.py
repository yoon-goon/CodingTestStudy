# https://www.acmicpc.net/problem/18258
import sys
from collections import deque


n = int(input())
que = deque()

for _ in range(n):
    x = list(sys.stdin.readline().split())
    if x[0] == 'push':
        que.append(x[1])
        print(que[-1])
    elif x[0] == 'pop':
        if que == False:
            print(-1)
        else:
            print(que.pop())
    elif x[0] == 'size':
