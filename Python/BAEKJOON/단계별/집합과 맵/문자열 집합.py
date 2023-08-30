# https://www.acmicpc.net/problem/14425
import sys

n, m = map(int,input().split())
own = []

for _ in range(n):
    own.append(sys.stdin.readline().strip())

print(own)
