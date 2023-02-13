# https://www.acmicpc.net/problem/1065

N = int(input())
cnt = 0

for i in range(1, N + 1):
    if i < 100:
        cnt += 1
    elif 110 < i < 1000:
        a = str(i)
        if int(a[1]) - int(a[0]) == int(a[2]) - int(a[1]):
            cnt += 1

print(cnt)
