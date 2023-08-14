# https://www.acmicpc.net/problem/25305
import sys

n, k = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().strip().split()))

print(sorted(x, reverse=True)[k - 1])

'''
c.sort()
print(c[-b])
로 간단하게 구현 가능
'''