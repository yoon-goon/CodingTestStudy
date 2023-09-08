# https://www.acmicpc.net/problem/1269
import sys

# 시간초과
'''
aNum, bNum = map(int, input().strip().split())

a = list(sys.stdin.readline().split())
b = list(sys.stdin.readline().split())
ac = len(a)
bc = len(b)

for i in b:
    if i in a:
        ac -= 1

for i in a:
    if i in b:
        bc -= 1

print(ac + bc)
'''

aNum, bNum = map(int, input().strip().split())

a = list(sys.stdin.readline().split())
b = list(sys.stdin.readline().split())

all = set(a + b)

print(len(all) * 2 - len(a) - len(b))
