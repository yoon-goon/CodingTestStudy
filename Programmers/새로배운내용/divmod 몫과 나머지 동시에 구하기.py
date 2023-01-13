a = 8
b = 5

print(a // b, a % b)  # / 두개로 소숫점없이 몫만 구할수 있음

print(divmod(a, b))

print(*divmod(a, b))  # 를 이용해 언패킹

c, d = divmod(14, 5)
print(c, d)
