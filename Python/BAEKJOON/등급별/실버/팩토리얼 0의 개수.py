# https://www.acmicpc.net/problem/1676

def fac(n):
    if n == 0 or n == 1:
        return 1
    return n * fac(n - 1)


n = int(input())
num = str(fac(n))
print(num)
ans = 0

for i in num:
    if i == str(0):
        ans += 1

print(ans)
