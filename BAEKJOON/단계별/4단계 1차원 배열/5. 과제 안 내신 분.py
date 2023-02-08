# https://www.acmicpc.net/problem/5597
import sys

list = []
answer = []
for i in range(28):
    list.append(int(sys.stdin.readline()))

for y in range(1, 31):
    if y not in list:
        answer.append(y)

print(min(answer))
print(max(answer))
