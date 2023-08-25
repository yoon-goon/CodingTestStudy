# https://www.acmicpc.net/problem/1181
import sys

n = int(input())
lst = []

for _ in range(n):
    x = sys.stdin.readline().strip()
    if x in lst:
        pass
    else:
        lst.append(x)
print(lst)

lst.sort(key=len())

for i in lst:
    print(i)
