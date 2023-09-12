# https://www.acmicpc.net/problem/1735
import sys
import math

a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())

upper = a1 * b2 + a2 * b1
lower = b1 * b2

i = math.gcd(upper, lower)
print(upper // i, lower // i)
'''
# 시간초과로 인해 직접구현대신 math 함수 사용
for i in range(min(upper, lower), 0, -1):
    if (upper % i == 0) and (lower % i == 0): # i = 최대공약수
        print(upper // i, lower // i)
        break
'''
