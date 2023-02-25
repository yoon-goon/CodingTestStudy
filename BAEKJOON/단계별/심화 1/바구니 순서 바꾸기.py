# https://www.acmicpc.net/problem/10812
import sys

N, M = map(int, input().split())
ans = list(range(1, N + 1))

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    ans[i - 1:k], ans[k:j + 1] = ans[j:k - 1:-1], ans[k - 1:i - 1:-1]

print(*ans)
