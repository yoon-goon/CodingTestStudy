# https://www.acmicpc.net/problem/28278
import sys

n = int(input())

stack = []

for i in range(n):
    a = int(sys.stdin.readline())
    if a == 1:
        x = int(sys.stdin.readline())
        stack.append(x)
    elif a == 2:
        print(stack[-1])

