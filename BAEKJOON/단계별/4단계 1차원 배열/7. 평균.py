# https://www.acmicpc.net/problem/1546
import sys

_num = int(input())
numlist = (sys.stdin.readline().split())
answer = 0

for i in range(_num):
    answer += int(numlist[i]) / int(max(numlist)) * 100

print(answer / _num)
