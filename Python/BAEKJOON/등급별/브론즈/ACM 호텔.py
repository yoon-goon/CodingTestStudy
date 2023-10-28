# https://www.acmicpc.net/problem/10250
import sys

t = int(input())

for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().split())

    f = n % h
    room = (n // h) + 1

    print(f*100+room)
