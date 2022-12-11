# https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        count = 0
        for j in range(i):
            if i % (j+1) == 0:
                count += 1
        if count % 2 == 0:
            answer += i
        else:
            answer -= i



    return answer

print(solution(13,17))