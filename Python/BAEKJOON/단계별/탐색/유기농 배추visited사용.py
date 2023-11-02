# https://www.acmicpc.net/problem/1012
import sys

input = sys.stdin.readline

dirR = [1, -1, 0, 0]  # row
dirC = [0, 0, 1, -1]  # col


def dfs(y, x):
    global visit
    visit[y][x] = 1
    for dirIdx in range(4):
        newY = y + dirR[dirIdx]
        newX = x + dirC[dirIdx]
        if graph[newY][newX] == 1 and visit[newY][newX] == 0:
            dfs(newY, newX)


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * 51 for _ in range(51)]  # 최대가 50까지라했으나 +1하고 사용할거기 때문
    visit = [[0] * 51 for _ in range(51)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y + 1][x + 1] = 1

    answer = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if graph[i][j] == 1 and visit[i][j] == 0:
                dfs(i, j)
                answer += 1

    print(answer)