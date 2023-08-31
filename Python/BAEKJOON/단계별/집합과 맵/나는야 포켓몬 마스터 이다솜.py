# https://www.acmicpc.net/problem/1620
import sys

n, m = map(int, sys.stdin.readline().strip().split())
poke = []

for i in range(n):
    poke.append(sys.stdin.readline().strip())

print(poke)
