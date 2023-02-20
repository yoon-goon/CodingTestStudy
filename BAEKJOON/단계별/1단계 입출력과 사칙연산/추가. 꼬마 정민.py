# https://www.acmicpc.net/problem/11382
import sys

A, B, C = map(int, sys.stdin.readline().split())

print(A + B + C)

# 간략화

print(sum(map(int,input().split())))