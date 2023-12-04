# https://www.acmicpc.net/problem/28278
import sys

n = int(input())
stack = []

for i in range(n):
    a = list(map(int, sys.stdin.readline().strip().split()))
    if a[0] == 1:
        stack.append(a[1])
    elif a[0] == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif a[0] == 3:
        print(len(stack))
    elif a[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 5:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

