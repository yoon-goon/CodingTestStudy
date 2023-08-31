# https://www.acmicpc.net/problem/7785
import sys

n = int(input())
lst = []

for i in range(n):
    x, y = sys.stdin.readline().split()
    if y == "enter":
        lst.append(x)
    else:
        lst.pop(x)