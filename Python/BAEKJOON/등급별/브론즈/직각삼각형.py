# https://www.acmicpc.net/problem/4153
import sys

a, b, c = map(int, sys.stdin.readline().split())

while a != 0 or b != 0 or c != 0:
    if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print('right')
    else:
        print('wrong')
    a, b, c = map(int, sys.stdin.readline().split())