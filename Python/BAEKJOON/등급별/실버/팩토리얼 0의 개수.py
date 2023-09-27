# https://www.acmicpc.net/problem/1676

def fac(n):
    if n == 0 or n == 1:
        return 1
    return n * fac(n - 1)


n = int(input())
num = fac(n)
print(num)
ans = 0

for i in range(len(num)):
    if num[i] == 0:
        ans += 1

print(ans)
