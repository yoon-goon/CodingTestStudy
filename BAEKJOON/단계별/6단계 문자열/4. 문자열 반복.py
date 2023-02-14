# https://www.acmicpc.net/problem/2675
import sys

test_num = int(input())
for i in range(test_num):
    times, words = sys.stdin.readline().split(' ')
    for y in words:
        for x in range(int(times)):
            print(y, end=''.rstrip())
