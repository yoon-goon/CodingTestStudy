# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    all = brown + yellow
    width = 1
    length = 0
    while width > length:
        width = int(all / (length+1))
        length += 1



    return [width,length]


print(solution(10,2))
print(solution(8,1))
print(solution(24,24))