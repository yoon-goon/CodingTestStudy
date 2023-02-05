'''
백준 3단계 A+B - 7 에서 사용된 예시


import sys

time = int(input())
for i in range(1, time + 1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #" + str(i) + ": " + str(a + b))
    print(f"Case #{i}: {a+b}") # 이런 문법으로 작성가능

'''


c = 500
d = 600

print(str(c)+"와 "+str(d)+"의 합산은 = "+str(c+d))
# 를 {}를 이용해 이렇게 변경 가능
print(f"{c}와 {d}의 합산은 = {c+d}")

