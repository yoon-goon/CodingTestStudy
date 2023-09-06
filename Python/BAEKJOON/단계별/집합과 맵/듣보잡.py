# https://www.acmicpc.net/problem/
import sys

n, m = input().strip().split()
nohear = []
nosee = []
ans = []

for _ in range(int(n)):
    nohear.append(sys.stdin.readline().strip())

for _ in range(int(m)):
    nosee.append(sys.stdin.readline().strip())

print(nohear,nosee)

for i in nohear:
    if i in nosee:
        print()