# https://www.acmicpc.net/problem/13241
import sys

a, b = map(int, sys.stdin.readline().strip().split())

for i in range(min(a, b), 0, -1):  # 최대공약수
    if (a % i == 0) and (b % i == 0):
        lcm = a * b // i  # 최대공약수를 이용해 최소공배수 구하기
        print(lcm)