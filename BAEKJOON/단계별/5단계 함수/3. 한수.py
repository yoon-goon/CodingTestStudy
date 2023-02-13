# https://www.acmicpc.net/problem/1065

N = int(input())
cnt = 0

for i in range(1, N + 1):
    if i < 100:     # 1~9까지 모두 한수, 10~99까지도 모두 한수 (2 자릿수까지는 모두 두 수의 차이가 한번밖에 없기에 성립)
        cnt += 1
    elif 110 < i < 1000:
        a = str(i)
        if int(a[1]) - int(a[0]) == int(a[2]) - int(a[1]):
            cnt += 1

print(cnt)
