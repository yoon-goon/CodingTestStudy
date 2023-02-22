# https://www.acmicpc.net/problem/10810
import sys

N, M = map(int, input().split())
ans = [0] * N  # N의 개수만큼 리스트에 아무 공도 들어가지 않은 자리인 0 생성해 두기 위함
for y in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for x in range(i - 1, j):
        ans[x] = k

print(*ans)  # 언패킹
