# https://www.acmicpc.net/problem/1934

case = int(input())

for _ in range(case):
    a, b = map(int, input().strip().split())
    for i in range(min(a, b), 0, -1):  # 최대공약수
        if (a % i == 0) and (b % i == 0):
            lcm = a * b // i # 최대공약수를 이용해 최소공배수 구하기
            print(lcm)
            break

''' #시간초과
for _ in range(case):
    a, b = map(int, input().strip().split())
    for i in range(max(a, b), a * b + 1):  # 둘중에 큰숫자부터 시작해서 최대 a*b
        if (i % a == 0) and (i % b == 0):
            print(i)
            break
'''
