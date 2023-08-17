# https://www.acmicpc.net/problem/10989 카운팅 정렬을 사용하는 문제
import sys

n = int(sys.stdin.readline())

lst = [0] * 10001

for _ in range(n):
    a = int(sys.stdin.readline())
    lst[a] += 1

for i in range(10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)
