# https://www.acmicpc.net/problem/1157

ans = list(str(input().upper()))
set_ans = set(ans)
cnt = []
list_ans = list(set_ans)
for i in set_ans:
    cnt.append(ans.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(list_ans[cnt.index(max(cnt))])
