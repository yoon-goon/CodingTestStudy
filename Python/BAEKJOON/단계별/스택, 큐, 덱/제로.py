# https://www.acmicpc.net/problem/10773
import sys

k = int(input())

stack = []
for _ in range(k):
    a = int(sys.stdin.readline())
    if a != 0:
        stack.append(a)
    else:
        stack.pop()

print(sum(stack))