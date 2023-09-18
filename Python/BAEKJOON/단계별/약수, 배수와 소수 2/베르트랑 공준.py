# https://www.acmicpc.net/problem/4948
import sys

def prime(x):
    if x < 2:  # 만약 2보다 작으면 소수가 아니므로 False 반환
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

lst = []
for y in range(1,246913):
    if prime(y):
        lst.append(1)
    else:
        lst.append(0)
print(lst)


# n = int(sys.stdin.readline())  # n<x<=2
# while n != 0:
#     num = 0
#     for i in range(n + 1, 2*n+1):
#         if prime(i):
#             num += 1
#     print(num)
#     n = int(sys.stdin.readline())
