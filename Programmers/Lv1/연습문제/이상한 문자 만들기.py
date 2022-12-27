# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ''
    newlist = s.split(' ')
    for i in newlist:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '

    return answer


print(solution("try hello world"))
