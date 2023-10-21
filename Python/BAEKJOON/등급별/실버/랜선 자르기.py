# https://www.acmicpc.net/problem/1654
import sys

n, k = map(int, sys.stdin.readline().split())

lst = []

for i in range(n):
    lst.append(int(sys.stdin.readline()))

#이진탐색을 위한 세팅
start = 1
end = max(lst)

while start <= end:
    mid = (start+end) // 2
    lines = 0
    for y in lst:
        lines += (y//mid)
        print(lines)
