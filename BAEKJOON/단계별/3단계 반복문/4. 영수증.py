# https://www.acmicpc.net/problem/25304

total = int(input())
num = int(input())
money = 0

for i in range(num):
    a, b = map(int, input().split())
    money += a*b

if money == total:
    print("Yes")
else:
    print("No")
