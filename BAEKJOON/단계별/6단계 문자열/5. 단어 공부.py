# https://www.acmicpc.net/problem/1157

ans = list(str(input().upper()))
set_ans = set(ans)
cnt = []
for i in set_ans:
    cnt.append(ans.count(i))



print(set_ans)
print(cnt)
