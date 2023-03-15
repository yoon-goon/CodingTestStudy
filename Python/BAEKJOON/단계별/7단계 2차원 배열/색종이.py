# https://www.acmicpc.net/problem/2563
import sys

space = [[0] * 100 for _ in range(100)]

papers = int(input())
for _ in range(papers):
    A, B = map(int, sys.stdin.readline().split())
    for i in range(A, A + 10):
        for y in range(B, B + 10):
            space[i][y] = 1

cnt = 0
for x in range(100):
    for w in range(100):
        if space[x][w] == 1:
            cnt += 1

print(cnt)
