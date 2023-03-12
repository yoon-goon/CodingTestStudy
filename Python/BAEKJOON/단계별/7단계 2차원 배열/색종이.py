# https://www.acmicpc.net/problem/2563
import sys

space = []
for i in range(100):
    space.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


papers = int(input())
for _ in range(papers):
    A, B = map(int, sys.stdin.readline().split())
    for y in range(A,A+10):
        space[B][y] = 1


print(space)
