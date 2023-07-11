# https://www.acmicpc.net/problem/14215
import sys

a, b, c = map(int, sys.stdin.readline().split())

alist = [a, b, c]

maxnum = max(alist)
minnum = min(alist)

alist.remove(maxnum)

if sum(alist) > maxnum:
    print(sum(alist) + maxnum)
    print("if")
else:
    print(alist)
    print(sum(alist)*2-1)