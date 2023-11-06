# https://www.acmicpc.net/problem/15829
import sys

input = sys.stdin.readline

l = int(input())
num = input()
ans = 0

for i in num:
    x = ord[i] - ord['a'] + 1
