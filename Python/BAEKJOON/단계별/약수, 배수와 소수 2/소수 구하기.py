# https://www.acmicpc.net/problem/1929
import sys


def prime(x):
    if x < 2:  # 만약 2보다 작으면 소수가 아니므로 False 반환
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


n, m = map(int, sys.stdin.readline().split())

for i in range(n, m + 1):
    if prime(i):
        print(i)
