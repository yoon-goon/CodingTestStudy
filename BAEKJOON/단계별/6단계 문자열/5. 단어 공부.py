# https://www.acmicpc.net/problem/1157

ans = list(str(input().upper()))
anslist = []

for i in ans:
    anslist.append(ans.count(i))

print(anslist)
print(max(anslist))
print(anslist.index(max(anslist)))
