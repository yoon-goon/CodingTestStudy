# https://www.acmicpc.net/problem/2609

a, b = list(map(int, input().split()))


def GCD(x, y):  # 최소공배수(Greatest Common Divisor)
    while (y):
        z = y # 값 저장
        y = x % y
        x = z
    return x


def LCM(x, y):  # 최대공약수(Least Common Multiple)
    result = (x * y) // GCD(x, y)
    return result


print(GCD(a, b))
print(LCM(a, b))
