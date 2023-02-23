# https://www.acmicpc.net/problem/10811
import sys

N, M = map(int, input().split())
ans = [0]
for i in range(1, N + 1):
    ans.append(i)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    ans[i:j] = reversed(ans[i:j])
    print(ans)

print(ans)
