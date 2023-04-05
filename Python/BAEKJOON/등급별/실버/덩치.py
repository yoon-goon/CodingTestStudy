#
import sys

N = int(input())
e_list = []

for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    e_list.append([A,B])


print(e_list)