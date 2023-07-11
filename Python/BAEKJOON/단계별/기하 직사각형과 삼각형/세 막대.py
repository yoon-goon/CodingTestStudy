# https://www.acmicpc.net/problem/14215
import sys

a, b, c = map(int, sys.stdin.readline().split())

alist = [a, b, c]

maxnum = max(alist)
minnum = min(alist)

alist.remove(maxnum)

if sum(alist) > maxnum:
    print(sum(alist) + maxnum)
else:
    print(sum(alist) * 2 - 1)


# 간단한 풀이
li = sorted(map(int, input().split()))
res = li[0] + li[1] + min(li[2], li[0]+li[1]-1)
print(res)
