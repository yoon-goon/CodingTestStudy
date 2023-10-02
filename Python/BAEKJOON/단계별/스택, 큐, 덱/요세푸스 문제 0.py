# https://www.acmicpc.net/problem/11866

n, k = map(int, input().split())

stack = []

for i in range(1,n+1):
    stack.append(i)

print(stack)