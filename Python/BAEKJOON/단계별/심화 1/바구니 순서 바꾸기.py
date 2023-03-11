# https://www.acmicpc.net/problem/10812
import sys

N, M = map(int, input().split())
ans = list(range(1, N + 1))

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    left = ans[:i - 1]
    mid1 = ans[i - 1:k - 1]
    mid2 = ans[k - 1:j]
    right = ans[j:]
    ans = left + mid2 + mid1 + right

print(*ans)
### 개선풀이
import sys

N, M = map(int, input().split())
ans = list(range(1, N + 1))

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    ans[i - 1:j] = ans[k - 1:j] + ans[i - 1:k - 1]
print(*ans)
