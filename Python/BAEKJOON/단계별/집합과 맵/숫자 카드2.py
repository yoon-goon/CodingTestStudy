# https://www.acmicpc.net/problem/10816

import sys

input()
own = set(map(int, sys.stdin.readline().split())) # 시간초과로 인해 set로 변경
input()
compare = list(map(int, sys.stdin.readline().split()))