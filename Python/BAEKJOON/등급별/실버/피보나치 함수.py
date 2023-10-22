# https://www.acmicpc.net/problem/1003
import sys

def fibo(x):
    if x == 0:
        print(0)
        return 0
    elif x == 1:
        print(1)
        return 1
    else:
        return fibo(x-1) + fibo(x-2)



t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline())
