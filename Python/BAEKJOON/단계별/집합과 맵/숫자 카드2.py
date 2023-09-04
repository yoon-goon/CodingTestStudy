# https://www.acmicpc.net/problem/10816
import sys

n = int(input())
own = list(map(int, sys.stdin.readline().split()))
m = int(input())
compare = list(map(int, sys.stdin.readline().split()))
result = [0] * m

for i in own:
    if i in compare:
        result[compare.index(i)] += 1

print(*result)
