# https://www.acmicpc.net/problem/18870
import sys

N = int(sys.stdin.readline())

# 자신보다 작은 수 갯수를 출력하면 됨

xlist = list(map(int, sys.stdin.readline().split()))
xset = list(set(xlist))

# print(xlist)

for i in xlist:
    cnt = 0
    for y in range(len(xset)):
        if i > xset[y]:
            cnt += 1
    print(cnt, end=' ')






'''
N = int(input())

# 자신보다 작은 수 갯수를 출력하면 됨

xlist = list(map(int, input().split()))
xset = list(set(xlist))

# print(xlist)

for i in xlist:
    cnt = 0
    for y in range(len(xset)):
        if i > xset[y]:
            cnt += 1
    print(cnt, end=' ')
    
    #시간초과된 풀이
'''

