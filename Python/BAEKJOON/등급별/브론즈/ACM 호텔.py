# https://www.acmicpc.net/problem/10250
import sys

t = int(input())

for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().split())

    f = n % h
    if f != 0:
        room = (n // h) + 1
    else:  # 딱 나눠떨어지면 최대층수를 사용하면 됨
        f = h
        room = (n // h)

    print(f * 100 + room)
