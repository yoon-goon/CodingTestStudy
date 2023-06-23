# https://www.acmicpc.net/problem/11005

N, a = map(int,input().split())  # N 진법

lst = []

while N != 0:
    b = N % a
    if a >= 10:
        lst.append(chr(b+55))
    else:
        lst.append(str(b))
    N = N // a

print(*lst)

