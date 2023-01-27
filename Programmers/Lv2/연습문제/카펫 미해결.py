# https://school.programmers.co.kr/learn/courses/30/lessons/42842

'''
def solution(brown, yellow): #잘못된 알고리즘, 새로 작성해야함
    answer = []
    all = brown + yellow
    width = 2
    length = 1
    while width > length:
        if all % length == 0:
            length += 1
            width = int(all / (length))
        else:
            length += 1
            continue

    return [max(width,length), min(width,length)]
'''
def solution(brown, yellow):
    answer = []
    _all = brown+yellow



print(solution(10, 2))
print(solution(8,1))
print(solution(24,24))