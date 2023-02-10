# https://www.acmicpc.net/problem/8958
import sys

time = int(input())
answer = 0

for i in range(time):
    numlist = (sys.stdin.readline())
    for y in range(len(numlist)-1,-1,-1):
        if numlist[y] == "O":
            b = y
            while numlist[b] == "O":
                b -= 1
                answer += 1


        print(numlist[y])

print(answer)

