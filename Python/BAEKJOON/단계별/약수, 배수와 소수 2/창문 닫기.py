# https://www.acmicpc.net/problem/13909
import sys

n = int(sys.stdin.readline())
cnt = 0

for i in range(1, n + 1): # 브루트포스로 진행하면 초과 발생
    if i ** 2 <= n:
        cnt += 1
print(cnt)


