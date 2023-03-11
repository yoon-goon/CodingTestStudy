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
list_ans = list(set(ans)) # 중복 제거
cnt = []
for i in list_ans:
    cnt.append(ans.count(i)) # ans 에서 list_ans 의 요소를 카운트해 cnt 배열에 append

if cnt.count(max(cnt)) > 1: # cnt 배열에 최대값이 2개 이상일 경우 ? 출력
    print('?')
else:
    print(list_ans[cnt.index(max(cnt))]) # 아닐경우 최대값의 인덱스를 통해 list_ans에서의 값 출력