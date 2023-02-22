# https://www.acmicpc.net/problem/10813
import sys

N, M = map(int, input().split())
ans = []
for x in range(1, N + 1):
    ans.append(x)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    ans[i - 1], ans[j - 1] = ans[j - 1], ans[i - 1]
    print(ans)

print(*ans)
