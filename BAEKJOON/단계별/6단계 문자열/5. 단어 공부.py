# https://www.acmicpc.net/problem/1157

'''


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

'''

# 불필요한 코드 줄이기

ans = list(str(input().upper()))
list_ans = list(set(ans))
cnt = []
for i in list_ans:
    cnt.append(ans.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(list_ans[cnt.index(max(cnt))])