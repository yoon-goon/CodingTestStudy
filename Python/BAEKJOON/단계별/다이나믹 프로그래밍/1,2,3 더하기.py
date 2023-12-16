# https://www.acmicpc.net/problem/9095
import sys

t = int(input())

for _ in range(t):
    n = int(sys.stdin.readline())
    dp = [0] * (n + 1)

    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 2
    if n >= 3:
        dp[3] = 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    print(dp[n])

'''
피보나치 수열과 비슷함
기본값을 설정해준 이후론 공식에 따라가면 됨
'''