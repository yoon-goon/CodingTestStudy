# https://school.programmers.co.kr/learn/courses/30/lessons/76501

true = 1
false = -1


def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == -1:
            absolutes[i] = absolutes[i] * -1

    return sum(absolutes)


print(solution([4, 7, 12], [true, false, true]))
