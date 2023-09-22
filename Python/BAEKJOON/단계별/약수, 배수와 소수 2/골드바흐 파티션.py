# https://www.acmicpc.net/problem/17103
import sys

input = sys.stdin.readline

lst = [False, False] + [True] * 999999
# 리스트에 0,1번에는 False, 2번부터는 True 대입.
# Index번호는 숫자를 의미하고, Index의 값은 소수인지 아닌지를 판별함.

for i in range(2, 1000001):
    if lst[i] == True:
        for j in range(i * 2, 1000001, i):  # i 가 소수인경우 그 배수들은 모두 소수일수가 없으므로
            lst[j] = False

T = int(input())

for y in range(T):
    cnt = 0
    n = int(input())
    for x in range(len(lst)):
        if lst[x] and lst[n - x]:
            cnt += 1
    print(cnt)

