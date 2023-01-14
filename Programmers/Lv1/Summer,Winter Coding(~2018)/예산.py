# https://school.programmers.co.kr/learn/courses/30/lessons/12982


def solution(d, budget):
    count = 0
    d = sorted(d)
    for i in range(len(d)):
        if budget >= d[i]:
            budget = budget - d[i]
            count += 1
    return count


print(solution([1,3,2,5,4],9))