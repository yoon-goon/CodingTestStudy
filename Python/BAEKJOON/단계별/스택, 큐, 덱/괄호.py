# https://www.acmicpc.net/problem/9012
import sys

t = int(input())

for _ in range(t):
    r = 0
    l = 0
    a = sys.stdin.readline()
    for i in a:
        if r >= 0:
            if i == "(":
                r += 1
            else:
                l += 1

    if r == l:
        print('YES')
    else:
        print('NO')
