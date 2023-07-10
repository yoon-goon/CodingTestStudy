# https://www.acmicpc.net/problem/5073



while a == 0 and b == 0 and c == 0:
    a = int(input())
    b = int(input())
    c = int(input())

    if a == b and b == a and c == a:
        print("Equilateral")
    elif a + b + c == 180:
        aset = set()
        aset.update([a, b, c])
        if len(aset) == 2:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Error")
