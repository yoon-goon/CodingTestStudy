# https://www.acmicpc.net/problem/24267

n = int(input())
count = 0

for i in range(n - 2):
    j = i + 1
    for j in range(n - 1):
        k = j + 1
        for k in range(n):
            count += 1

print(count, "\n3")

print(n * n * n, "\n3")

'''
예제
7

---
35
3
'''