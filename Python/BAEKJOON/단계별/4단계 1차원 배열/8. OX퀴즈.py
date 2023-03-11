# https://www.acmicpc.net/problem/8958
import sys

time = int(input())

for i in range(time):
    answer = 0
    numlist = (sys.stdin.readline())
    for y in range(len(numlist) - 1, -1, -1):
        if numlist[y] == "O":
            b = y
            while numlist[b] == "O":
                b -= 1
                answer += 1
    print(answer)

'''
while을 사용하지 않고 ,split('X')로 X 마다 요소를 나누어 계산하는 방법도 있음

for _ in range(int(sys.stdin.readline())):
    point = 0
    for x in str(sys.stdin.readline())[:-1].split('X'):
        point += len(x)*(len(x)+1)//2
    print(point)


'''