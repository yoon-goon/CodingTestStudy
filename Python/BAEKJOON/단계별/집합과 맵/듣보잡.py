# https://www.acmicpc.net/problem/
import sys

n, m = input().strip().split()
nohear = []
nosee = []
ans = []

for _ in range(int(n)):
    nohear.append(sys.stdin.readline().strip())
for _ in range(int(m)):
    nosee.append(sys.stdin.readline().strip())

''' # 시간초과 발생
for i in nohear:
    if i in nosee:
        ans.append(i)
'''

ans = list(set(nohear) & set(nosee)) #  set의 & 연산자는 두 집합의 교집합을 반환

print(len(ans))
for i in sorted(ans):
    print(i)
