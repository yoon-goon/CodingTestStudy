# https://www.acmicpc.net/problem/10816
import sys

int(sys.stdin.readline())
own = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
compare = list(map(int, sys.stdin.readline().split()))
result = [0] * m

for i in own:
    if i in compare:
        result[compare.index(i)] += 1

print(*result)
