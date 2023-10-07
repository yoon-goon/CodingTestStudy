# https://www.acmicpc.net/problem/12789
import sys
from collections import deque

n = int(input())
x = list(map(int,sys.stdin.readline().split()))
a = 1
que = deque()
line = []

for i in x:
    if i == a:
        line.append(i)
        a += 1
    elif len(que) > 0:
        if que[-1] == a:
            line.append(i)
            que.pop()
            a += 1
    else:
        que.append(i)

for _ in range(len(que)):
    b = que.pop()
    if a == b:
        line.append(b)
        a += 1
    else:
        print("Sad")
        break

print(line)
print(que)

if len(line) == n:
    print("Nice")

