# https://www.acmicpc.net/problem/2563
import sys

space = []
for i in range(10):
    space.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

print(space[1][2])

papers = int(input())
for _ in range(papers):
    A, B = map(int, sys.stdin.readline().split())
