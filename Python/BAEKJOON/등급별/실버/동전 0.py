# https://www.acmicpc.net/problem/11047
import sys

kind, csum = map(int, input().split())
coinL = []
print(kind, csum)

for i in range(kind):
    coinL.append(sys.stdin.readline().strip())

print(coinL)

for i in range(kind,0,-1):
    print(i)