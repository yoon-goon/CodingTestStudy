# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = s.split(" ")
    #for i in range(len(answer)):
    #    answer[i] = int(answer[i])

    return min(answer)+" "+max(answer)


print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))