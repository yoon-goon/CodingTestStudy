# https://www.acmicpc.net/problem/2839

n = int(input())

bags = 0

while n >= 0:
    if n % 5 == 0:
        bags += n // 5
