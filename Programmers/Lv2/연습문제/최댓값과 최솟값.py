# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    numlist = []
    answer = s.split(" ")
    print(answer)
    for i in answer:
        numlist.append(int(i))


    return str(min(numlist))+" "+str(max(numlist))


print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))