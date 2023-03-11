# https://www.acmicpc.net/problem/1152
import sys

words = sys.stdin.readline().strip().split(" ")
if words == ['']: # 입력값이 공백만 있는경우 처리를 위해
    print('0')
else:
    print(len(words))

