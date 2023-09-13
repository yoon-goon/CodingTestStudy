# https://www.acmicpc.net/problem/2485
import sys
import math

n = int(sys.stdin.readline())

a = int(sys.stdin.readline())
lst = [a]
distance = []  # 간격
for _ in range(n - 1):
    b = int(sys.stdin.readline())
    lst.append(b)
    distance.append(b - a)
    a = b

print(lst)
print(distance)

gcd = math.gcd(*distance)
print(gcd)

to_add = ((max(lst) - min(lst)) // gcd + 1 - n)
print(to_add)
