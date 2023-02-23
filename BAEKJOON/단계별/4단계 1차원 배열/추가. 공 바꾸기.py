# https://www.acmicpc.net/problem/10813
import sys

N, M = map(int, input().split())
ans = []
for x in range(1, N + 1):
    ans.append(x)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    ans[i - 1], ans[j - 1] = ans[j - 1], ans[i - 1] # 인덱스가 0부터 시작함으로 3번째 자리를 바꾸려면 4가 나와야해서 -1

print(*ans)
