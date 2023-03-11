# https://www.acmicpc.net/problem/15552
import sys

time = int(sys.stdin.readline())

for i in range(time):  # 반복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline()을 사용해야 시간초과가 발생하지않음
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
