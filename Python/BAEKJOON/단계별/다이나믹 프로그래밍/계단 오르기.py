# https://www.acmicpc.net/problem/2579
import sys

input = sys.stdin.readline

n = int(input())

stair = [0] * n

for i in range(n):
    stair[i] = int(input())

dp = [0] * n
dp[0] = stair[0]
dp[1] = stair[0]+stair[1]

