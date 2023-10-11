# https://www.acmicpc.net/problem/1259

a = input()

while a != '0':
    if a == a[::-1]:
        print("yes")
    else:
        print("no")
    a = input()