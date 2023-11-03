# https://www.acmicpc.net/problem/18110
import sys

input = sys.stdin.readline


def myRound(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)


n = int(input())
if n == 0:
    print(0)
else:
    lst = []

    for _ in range(n):
        lst.append(int(input()))
    lst.sort()
    # print(lst)
    cutline = myRound(len(lst) * 0.15)
    # print(cutline)
    if cutline != 0:
        croped = lst[cutline:-cutline]
        print(myRound(sum(croped) / len(croped)))
    else:
        print(myRound(sum(lst) / len(lst)))
