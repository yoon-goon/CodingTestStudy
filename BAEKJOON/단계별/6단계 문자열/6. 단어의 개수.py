# https://www.acmicpc.net/problem/1152
import sys

words = sys.stdin.readline().strip().split(" ")
if words == ['']:
    print('0')
else:
    print(len(words))

