# https://www.acmicpc.net/problem/10815
import sys

input()
own = set(map(int, sys.stdin.readline().split())) # 시간초과로 인해 set로 변경
input()
compare = list(map(int, sys.stdin.readline().split()))

for i in compare:
    if i in own:
        print("1 ", end='')
    else:
        print("0 ", end='')
