# https://www.acmicpc.net/problem/2475

lst = list(input().split())
every = 0

for i in lst:
    every += int(i) * int(i)

print(every % 10)
