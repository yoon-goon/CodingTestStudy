# https://www.acmicpc.net/problem/3052
import sys

numlist = []
answer = []
for i in range(10):
    numlist.append(int(sys.stdin.readline()) % 42)
for y in numlist:
    if y not in answer:
        answer.append(y)

print(len(answer))
