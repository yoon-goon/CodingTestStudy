# https://www.acmicpc.net/problem/11005

N, a = map(int, input().split())  # a 진법

lst = ''

while N != 0:
    b = N % a
    if a >= 10:
        lst += chr(b + 55)
    else:
        lst += str(b)
    N = N // a

print(lst[::-1])
