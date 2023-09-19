# https://www.acmicpc.net/problem/17103
import sys

input = sys.stdin.readline

lst = [False, False] + [True] * 999999
# 리스트에 0,1번에는 False, 2번부터는 True 대입.
# Index번호는 숫자를 의미하고, Index의 값은 소수인지 아닌지를 판별함.

T = int(input())

for i in range(T):
    n = int(input())
