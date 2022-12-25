# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    count = 0
    newarr = []
    for i in range(len(t) - (len(p)-1)):
        newarr.append(t[i:i + len(p)])
        if newarr[i] <= p:
            count += 1
    return count


print(solution("3141592","271"))
print(solution("500220839878","7"))
print(solution("10203", "15"))
