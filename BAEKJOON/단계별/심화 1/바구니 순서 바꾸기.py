# https://www.acmicpc.net/problem/10812
import sys

N, M = map(int, input().split())
ans = list(range(1, N + 1))

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    left = ans[:i]
    mid1 = ans[i:k]
    mid2 = ans[k:j+1]
    right = ans[j+1:]
    ans = left + mid2 + mid1 + right

print(*ans)
