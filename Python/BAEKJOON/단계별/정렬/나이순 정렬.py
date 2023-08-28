# https://www.acmicpc.net/problem/10814
import sys

n = int(input())
lst = []

for i in range(n):
    x, y = sys.stdin.readline().strip().split()
    if [x,y] in lst:
        pass
    else:
        lst.append([x, y])

lst.sort(key=lambda x: x[0])

for i in lst:
    print(*i)

'''
동명이인 처리를 추가해야함
시도 1 if [x,y] in lst
'''