# https://www.acmicpc.net/problem/4134
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a = int(sys.stdin.readline())
    while a != 0 and a != 1:
        for i in range(2, a ** 0.5 + 1): #루트
            if a%i == 0:
                print(a)
                break
