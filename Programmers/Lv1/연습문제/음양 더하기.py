# https://school.programmers.co.kr/learn/courses/30/lessons/76501
'''
true = 1
false = -1
'''


# 파이참에서는 돌아가나 채점 불가
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == -1:
            absolutes[i] = absolutes[i] * -1

    return sum(absolutes)


# 파이참에서는 안돌아가지만 채점 가능
def solution2(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer


# print(solution2([4, 7, 12], [true, false, true]))


# 해답 1 signs 인자를 수정해 해결한 버전
def solution3(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = absolutes[i] * -1

    return sum(absolutes)


print(solution3([4, 7, 12], [True, False, True]))
