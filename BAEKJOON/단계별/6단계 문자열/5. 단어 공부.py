# https://www.acmicpc.net/problem/1157

ans = list(str(input().upper()))
anslist = []
countlist = []

for i in ans:
    if not i in anslist:
        anslist.append(i)
    else:
        continue

print(anslist)
