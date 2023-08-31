# https://www.acmicpc.net/problem/7785
import sys

n = int(input())
log = set()

for i in range(n):
    x, y = sys.stdin.readline().split()
    if y == "enter":
        log.add(x)
    else:
        log.remove(x)

print(*sorted(log, reverse=True), sep='\n')
