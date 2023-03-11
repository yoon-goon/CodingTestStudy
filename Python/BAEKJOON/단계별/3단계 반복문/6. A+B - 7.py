# https://www.acmicpc.net/problem/11021
import sys

time = int(input())
for i in range(1, time + 1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #" + str(i) + ": " + str(a + b))
    print(f"Case #{i}: {a+b}") # 이런 문법으로 작성가능
