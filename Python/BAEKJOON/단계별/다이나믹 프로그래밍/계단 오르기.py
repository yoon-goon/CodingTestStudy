# https://www.acmicpc.net/problem/2579
import sys

input = sys.stdin.readline

n = int(input())

stair = [0] * (n + 10)

for i in range(n):
    stair[i] = int(input())

dp = [0] * (n + 10)
dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for y in range(3, n):
    dp[y] = max(dp[y - 3] + stair[y - 1] + stair[y], dp[y - 2] + stair[y])

print(dp[n - 1])
