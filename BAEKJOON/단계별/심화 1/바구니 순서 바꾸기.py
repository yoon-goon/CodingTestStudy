# https://www.acmicpc.net/problem/10812
import sys

N, M = map(int, input().split())
ans = []
for i in range(1, N + 1):
    ans.append(i)
print(*ans)

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    ans[i + 1:k + 1], ans[k + 1:j + 1] = ans[j + 1:k + 1:-1], ans[k + 1:i + 1:-1]

print(*ans)
