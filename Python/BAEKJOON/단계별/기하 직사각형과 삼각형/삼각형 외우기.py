# https://www.acmicpc.net/problem/10101

a = int(input())
b = int(input())
c = int(input())

if a == 60 and b == a and c == a:
    print("Equilateral")
elif a + b + c == 180 and 