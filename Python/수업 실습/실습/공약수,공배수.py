# 최대공약수(GCD)를 구하는 함수 (재귀적 구현)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 최소공배수(LCM)를 구하는 함수
def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(8,15))

print(lcm(8,15))