# https://www.acmicpc.net/problem/1012
import sys

sys.setrecursionlimit(10 ** 6)  # 재귀 깊이 제한

input = sys.stdin.readline

dirR = [1, -1, 0, 0]  # row
dirC = [0, 0, 1, -1]  # col


def dfs(y, x):
    graph[y][x] = 0  # visited를 1로 바꾸는 방식에서 graph를 0으로 지워나가게 변경
    for dirIdx in range(4):
        newY = y + dirR[dirIdx]
        newX = x + dirC[dirIdx]
        if graph[newY][newX] == 1:
            dfs(newY, newX)


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * (m + 2) for _ in range(n + 2)]  # 동적으로 배열 크기를 할당합니다.

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y + 1][x + 1] = 1

    answer = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if graph[i][j] == 1:
                dfs(i, j)
                answer += 1

    print(answer)
