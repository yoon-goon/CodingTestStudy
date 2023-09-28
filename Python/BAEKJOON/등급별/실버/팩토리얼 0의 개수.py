# https://www.acmicpc.net/problem/1676

def fac(n):
    if n == 0 or n == 1:
        return 1
    return n * fac(n - 1)


n = int(input())
num = str(fac(n))[::-1]
ans = 0

# 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 !!
for i in num:
    if i == str(0):
        ans += 1
    else:
        break

print(ans)