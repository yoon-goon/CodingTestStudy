# https://www.acmicpc.net/problem/2439

star = int(input())
for i in range(star):
    print(" " * (star - (i + 1)) + "*" * (i + 1))
