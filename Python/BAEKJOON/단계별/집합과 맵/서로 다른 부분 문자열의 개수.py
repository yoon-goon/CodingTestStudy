# https://www.acmicpc.net/problem/11478

S = input()
ans = set()

for i in range(len(S)):
    for y in range(i,len(S)):
        