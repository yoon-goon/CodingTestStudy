# https://www.acmicpc.net/problem/10814
import sys

n = int(input())
lst = []

for i in range(n):
    x, y = sys.stdin.readline().strip().split()
    lst.append([int(x), y])

lst.sort(key=lambda x: x[0])

for i in lst:
    print(*i)

'''

시도 1 동명이인 처리 if [x,y] in lst - 시간초과
시도 2 x인자를 int - 해결(동명이인 처리와 관련 없었음)

'''
