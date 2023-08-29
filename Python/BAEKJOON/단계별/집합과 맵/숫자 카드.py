# https://www.acmicpc.net/problem/10815
import sys

input()
own = list(map(int, sys.stdin.readline().split()))
input()
compare = list(map(int, sys.stdin.readline().split()))

for i in compare:
    if i in own:
        print("1 ", end='')
    else:
        print("0 ", end='')
