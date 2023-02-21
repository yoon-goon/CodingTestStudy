# https://www.acmicpc.net/problem/10810

N, M = map(int, input().split())
ans = [0] * N
for y in range(M):
    i, j, k = map(int, input().split())
    for x in range(i - 1, j):
        ans[x] = k

print(*ans)
