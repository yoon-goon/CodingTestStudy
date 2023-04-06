#
import sys

N = int(input())
e_list = []

for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    e_list.append([A,B])


for y in e_list:
    rank = 1
    for j in e_list:
        if y[0] < j [0] and y[1] < j[1]:
            rank += 1
    print(rank)

print(e_list)
print(e_list[0][0])