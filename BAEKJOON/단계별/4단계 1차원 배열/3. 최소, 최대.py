# https://www.acmicpc.net/problem/10818
import sys

total = int(input())
numlist = sys.stdin.readline().split()
answer = []

for i in range(total):
    answer.append(int(numlist[i]))

print(min(answer), max(answer))
