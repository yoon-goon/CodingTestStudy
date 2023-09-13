# https://www.acmicpc.net/problem/2485
import sys
import math

n = int(sys.stdin.readline())
a = int(sys.stdin.readline())
lst = [a] # 전체 리스트
distance = []  # 간격
for _ in range(n - 1):
    b = int(sys.stdin.readline())
    lst.append(b)
    distance.append(b - a)
    a = b

gcd = math.gcd(*distance) # 간격간 최대공약수

print(max(lst),min(lst),gcd,n)
to_add = ((max(lst) - min(lst)) // gcd + 1 - n)
# 최대값 - 최소값을 공약수로 나눈 후 n(초기에 입력받은 가로수의 수) 만큼 빼줘야함
print(to_add)
