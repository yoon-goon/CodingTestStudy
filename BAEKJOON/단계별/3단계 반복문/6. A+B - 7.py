# https://www.acmicpc.net/problem/11021
import sys

time = int(input())
for i in range(1, time + 1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #" + str(i) + ": " + str(a + b))
