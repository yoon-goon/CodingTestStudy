# https://www.acmicpc.net/problem/25314

num = int(input())
ans = ''
while num >= 4:
    num -= 4
    ans += 'long '

print(ans + 'int')
