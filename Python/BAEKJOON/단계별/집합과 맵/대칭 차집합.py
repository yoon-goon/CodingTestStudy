# https://www.acmicpc.net/problem/1269
import sys

aNum, bNum = map(int, input().strip().split())

a = list(sys.stdin.readline().split())
print(a)
b = list(sys.stdin.readline().split())
print(b)

ac = len(set(a+b))
bc = len(b)
for i in b:
    if i in a:
        ac = - 1
print(ac)
for i in a:
    if i in b:
        bc = - 1
print(bc)