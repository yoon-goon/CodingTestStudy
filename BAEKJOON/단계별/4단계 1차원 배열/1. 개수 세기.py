# https://www.acmicpc.net/problem/10807
import sys

total = int(input())
numlist = sys.stdin.readline().split()
find = input()
count = 0

for i in range(total):
    if numlist[i] == find:
        count += 1
print(count)
