# https://www.acmicpc.net/problem/2164


N = int(input())

alist = []

for i in range(1, N + 1):
    alist.append(i)

while len(alist) != 1:
    alist.remove(alist[0])
    alist.append(alist[0])
    alist.remove(alist[0])

print(*alist)

# 시간 초과