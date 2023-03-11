# https://school.programmers.co.kr/learn/courses/30/lessons/12969

a, b = map(int, input().strip().split(' '))
line = ""
for i in range(b):
    for y in range(a):
        line += "*"
    print(line)
    line = ""

''' 이런 풀이도 존재
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)
'''
'''
a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print('*', end='') # end를 이용해 print 출력후 한줄 띄워지는걸 방지 가능(''로 대체되는 예시)
    print('')
    
'''