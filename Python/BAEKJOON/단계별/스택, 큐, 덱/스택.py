# https://www.acmicpc.net/problem/10828
import sys

n = int(input())

stack = []

for _ in range(n):
    a = list(sys.stdin.readline().split())
    if a[0] == 'push':
        stack.append(a[1])
    elif a[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(stack))
    elif a[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif a[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
