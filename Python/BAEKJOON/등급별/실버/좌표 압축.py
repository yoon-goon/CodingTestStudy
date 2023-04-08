# https://www.acmicpc.net/problem/18870

N = int(input())

# 자신보다 작은 수 갯수를 출력하면 됨

xlist = list(map(int, input().split()))


print(xlist)

for i in N:
    cnt = 0
    for y in range(N):
        if i > xlist[y]:
            cnt += 1
