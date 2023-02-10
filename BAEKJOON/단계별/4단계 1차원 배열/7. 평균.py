# https://www.acmicpc.net/problem/1546
import sys


'''
_num = int(input())
numlist = list(map(int,sys.stdin.readline().split()))
answer = 0

for i in range(_num):
    answer += numlist[i] / max(numlist)*100

print(answer / _num)

'''

# 간략화 풀이

_num = int(input())
numlist = list(map(int,sys.stdin.readline().split()))
print(sum(numlist)/max(numlist)*100/_num)