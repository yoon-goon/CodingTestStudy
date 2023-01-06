# https://school.programmers.co.kr/learn/courses/30/lessons/12969

a, b = map(int, input().strip().split(' '))
line = ""
for i in range(b):
    for y in range(a):
        line += "*"
    print(line)
    line = ""
