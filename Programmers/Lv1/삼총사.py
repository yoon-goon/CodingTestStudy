# https://school.programmers.co.kr/learn/courses/30/lessons/131705

def solution(number):
    count = 0

    for i in range(len(number)):
        j = i + 1
        for j in range(j, len(number)):
            k = j + 1
            for k in range(k, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    count += 1

    return print(count)


solution([-2, 3, 0, 2, -5])
solution([-3, -2, -1, 0, 1, 2, 3])
solution([-1, 1, -1, 1])
