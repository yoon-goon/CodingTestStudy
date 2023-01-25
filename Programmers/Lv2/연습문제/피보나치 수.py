# https://school.programmers.co.kr/learn/courses/30/lessons/12945


def solution(n):  # 런타임 에러 발생,
    current, nextnum = 0, 1
    for i in range(n):
        current, nextnum = nextnum, current + nextnum  # 2 계산이 동시에 이뤄저야 하므로 ,로 같은줄에 작성
    return current


def better_solution(n):
    current, nextnum = 0, 1
    for i in range(n):
        current, nextnum = nextnum, current + nextnum  # 2 계산이 동시에 이뤄저야 하므로 ,로 같은줄에 작성
    return current % 1234567 # 문제의 내용에도 써있었고 %1234567을 통해 런타임 에러를 해결할 수있음
'''
https://mozzioi.tistory.com/147

'''


print(better_solution(3))
print(better_solution(5))
print(better_solution(500))
