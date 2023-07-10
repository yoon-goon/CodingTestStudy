# https://www.acmicpc.net/problem/5073

a, b, c = 1, 1, 1

while a != 0 and b != 0 and c != 0:
    a = int(input())
    b = int(input())
    c = int(input())

    if a == b and b == a and c == a:
        print("Equilateral")
    elif max(a, b, c) < a + b + c - max(a, b, c):
        aset = set()
        aset.update([a, b, c])
        if len(aset) == 2:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")
