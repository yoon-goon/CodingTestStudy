# https://www.acmicpc.net/problem/17219
import sys

n, m = map(int, input().split())
password = dict()

for i in range(n):
    a1, a2 = sys.stdin.readline().split()
    password[a1] = a2


for _ in range(m):
    b1 = sys.stdin.readline().strip()
    print(password[b1])

