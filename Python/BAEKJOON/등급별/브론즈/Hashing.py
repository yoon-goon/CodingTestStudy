# https://www.acmicpc.net/problem/15829
import sys

input = sys.stdin.readline

l = int(input())
num = input()
ans = 0

for i in range(l):
    x = ord(num[i]) - ord('a') + 1
    ans += x * (31 ** i)

print(ans % 1234567891)
