# https://www.acmicpc.net/problem/11478

S = input()
ans = set()

for i in range(len(S)):
    for y in range(i,len(S)):
        print(S[i:y+1])
        ans.add(S[i:y+1])

print(len(ans))