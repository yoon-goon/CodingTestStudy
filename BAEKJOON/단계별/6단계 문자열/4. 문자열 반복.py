# https://www.acmicpc.net/problem/2675

import sys

test_num = int(input())
for i in range(test_num):
    times, words = map(str,sys.stdin.readline().split())
    for y in words:
        for x in range(int(times)):
            print(y, end='')
    print('')




'''
for i in range(2):
    times, words = 3, 'ABC'
    for y in words:
        for x in range(int(times)):
            print(y, end='')
    print('')
'''