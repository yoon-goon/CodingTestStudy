# https://www.acmicpc.net/problem/2587
import sys

lst = []

for _ in range(5):
    lst.append(int(sys.stdin.readline().strip()))

print(int(sum(lst) / 5))
print(sorted(lst)[2])
