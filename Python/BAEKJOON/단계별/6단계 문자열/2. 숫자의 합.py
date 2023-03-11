# https://www.acmicpc.net/problem/11720
import sys

nums = int(input())

nlist = list(map(int, sys.stdin.readline().rstrip()))

print(sum(nlist))
