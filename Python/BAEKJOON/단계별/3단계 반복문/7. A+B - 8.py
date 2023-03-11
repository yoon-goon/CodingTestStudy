# https://www.acmicpc.net/problem/11022
import sys

time = int(input())

for i in range(time):
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case #{i + 1}: {a} + {b} = {a + b}")
