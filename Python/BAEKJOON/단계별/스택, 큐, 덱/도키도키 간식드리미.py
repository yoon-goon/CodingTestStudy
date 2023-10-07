# https://www.acmicpc.net/problem/12789
import sys
from collections import deque

n = int(input())
x = list(map(int,sys.stdin.readline().split()))
a = 1
que = deque()
line = []
print(x)

for i in x:
    if i == a:
        line.append(i)
        a += 1
    else:
        que.append(i)

print(line)
print(que)