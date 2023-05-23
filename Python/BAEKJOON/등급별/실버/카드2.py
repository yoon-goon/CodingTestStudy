# https://www.acmicpc.net/problem/2164


'''
N = int(input())

alist = []

for i in range(1, N + 1): // 이 부분을 최적화 할수 있을것 같음
    alist.append(i)

while len(alist) != 1:
    alist.remove(alist[0])
    alist.append(alist[0])
    alist.remove(alist[0])

print(*alist)

# 시간 초과

'''

# N = int(input())
# 
# alist = list(range(1, N + 1))
# 
# while len(alist) != 1: # 시간초과발생 구하는 방법을 개선해야할 것으로 보임
#     alist.remove(alist[0])
#     alist.append(alist[0])
#     alist.remove(alist[0])
# 
# print(*alist)


N = int(input())

alist = list(range(1, N + 1))

while len(alist) > 1:  # 시간초과발생 구하는 방법을 개선해야할 것으로 보임
    alist.remove(alist[0])
    alist.append(alist[0])
    alist.remove(alist[0])

print(*alist) # unpack

# 참고 https://my-coding-notes.tistory.com/83
