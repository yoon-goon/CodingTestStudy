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

print(len(ans))
for i in sorted(ans):
    print(i)
