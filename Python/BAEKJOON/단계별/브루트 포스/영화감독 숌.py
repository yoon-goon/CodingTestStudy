# https://www.acmicpc.net/problem/1436

n = int(input())
list = []

# print(str(n - 1) + '666')

for i in range(10000000):
    if '666' in str(i):
        list.append(i)

print()
