# https://www.acmicpc.net/problem/18258
import sys
from collections import deque

n = int(input())
que = deque()

for _ in range(n):
    x = list(sys.stdin.readline().split())
    if x[0] == 'push':
        que.append(x[1])
    elif x[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
    elif x[0] == 'size':
        print(len(que))
    elif x[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif x[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif x[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
