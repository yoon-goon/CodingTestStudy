# https://www.acmicpc.net/problem/18110
import sys

input = sys.stdin.readline


def myRound(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)


n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

print(lst)

cutline = myRound(len(lst) * 0.15)

print(cutline)

