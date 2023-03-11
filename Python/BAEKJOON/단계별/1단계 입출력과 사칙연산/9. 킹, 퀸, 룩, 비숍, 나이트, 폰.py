# https://www.acmicpc.net/problem/3003

answer = ''
b = input().split()
c = 1, 1, 2, 2, 2, 8
for i in range(len(b)):
    answer += str((c[i] - int(b[i]))) + ' '

print(answer.rstrip())
