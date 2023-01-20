# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    numlist = []
    answer = s.split(" ")
    for i in answer:
        numlist.append(int(i))

    return str(min(numlist)) + " " + str(max(numlist))

def solution2(s):
    answer = s.split(" ")
    answer = list(map(int,answer))
    return answer


print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))
print(solution2("1 2 3 4"))
print(solution2("-1 -2 -3 -4"))
print(solution2("-1 -1"))