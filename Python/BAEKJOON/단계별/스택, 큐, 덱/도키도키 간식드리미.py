# https://www.acmicpc.net/problem/12789
import sys
from collections import deque

#  스택, 큐 동시에 사용

n = int(input())
x = deque(map(int,sys.stdin.readline().split()))
stack = deque()
a = 1

while x: # x 에 있는 동안
    if x and x[0] == a:
        x.popleft() # 줄서잇는 순서로 먼저 나감으로
        a += 1
    else:
        stack.append(x.popleft())
    while stack and stack[-1] == a: # 뒷 순서부터 나감
        stack.pop()
        a += 1

if stack: # stack에 남아있다면
    print('Sad')
else:
    print('Nice')


'''
n = int(input())
x = list(map(int,sys.stdin.readline().split()))
a = 1
que = deque()
line = []
ans = 'Nice'

for i in x:
    if i == a:
        line.append(i)
        a += 1


    else:
        que.append(i)

print(line)
print(que)

for _ in range(len(que)):
    b = que.pop()
    if a == b:
        line.append(b)
        a += 1
    else:



print(line)
print(que)

print(ans)

'''