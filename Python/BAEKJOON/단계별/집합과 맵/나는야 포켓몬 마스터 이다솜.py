# https://www.acmicpc.net/problem/1620
import sys

n, m = map(int, sys.stdin.readline().strip().split())
poke = []

for i in range(n):
    poke.append(sys.stdin.readline().strip())

for y in range(m):
    x = sys.stdin.readline().strip()
    try:
        print(poke[int(x) - 1])
    except:
        print(poke.index(x) + 1)
