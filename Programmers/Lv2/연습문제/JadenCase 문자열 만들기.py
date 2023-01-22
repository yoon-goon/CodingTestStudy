# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    tmp = s.split(' ')
    for i in range(len(tmp)):
        tmp[i] = tmp[i].capitalize()
    return ' '.join(tmp)


print(solution("3people unFollowed me"))
print(solution("for the last week"))
