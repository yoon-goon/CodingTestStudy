# https://www.acmicpc.net/problem/1463

x = int(input())

dp = [0] * (x + 1)

for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1

    print(dp)

    if i % 2 == 0: # 2로 나눠떨어지면 2로 한 번 나눠줬으니 1을 더해서 (2로 나눈 정수의 연산 횟수 + 1)
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

'''
15 : 15 - 5 - 4 - 2 - 1 (4번)
5 : 5 - 4 - 2 - 1 (3번)
4 : 4 - 2 - 1 (2번)
2 : 2 - 1 (1번)
'''

print(dp[x])
