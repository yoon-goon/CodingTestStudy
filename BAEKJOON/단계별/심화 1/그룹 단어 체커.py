# https://www.acmicpc.net/problem/1316
import sys

nums = int(input())
cnt = 0

for _ in range(nums):
    words = sys.stdin.readline()
    for i in range(len(words)):
        