# https://www.acmicpc.net/problem/4134
import sys


def prime(x):
    if x < 2:# 만약 2보다 작으면 소수가 아니므로 False 반환
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False # 소수가 아니므로 False 반환
    return True


n = int(sys.stdin.readline())

for _ in range(n):
    a = int(sys.stdin.readline())

    if prime(a) == True:
        print(a)
    else:
        a += 1 # 다음숫자부터
        while True:
            if prime(a) == True:
                print(a)
                break
            a += 1
