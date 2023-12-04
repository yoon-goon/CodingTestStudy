# https://www.acmicpc.net/problem/10845

# 스택과 큐의 주요 차이점은 요소에 액세스하는 순서
# 스택은 LIFO (LAST in first out) 순서를 따르므로 스택에 마지막으로 추가된 요소가 가장 먼저 제거
# 반면에 큐는 (First In First Out) 순서

import sys

n = int(input())

que = []

for _ in range(n):
    a = list(sys.stdin.readline().split())
    if a[0] == 'push':
        que.append(a[1])
    elif a[0] == 'pop':
        if que:
            print(que.pop(0))
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(que))
    elif a[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
