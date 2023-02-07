# https://www.acmicpc.net/problem/10807
import sys

total = int(input())
numlist = sys.stdin.readline().split()
find = input()
cnt = 0

for i in range(total):
    if numlist[i] == find:
        cnt += 1
print(cnt)

print(numlist.count(find)) # count 를 사용해 훨씬 간단하게 해결할 수 있음
'''
배열.count(세고자 하는 원소) 
'''