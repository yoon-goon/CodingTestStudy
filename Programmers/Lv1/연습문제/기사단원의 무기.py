# https://school.programmers.co.kr/learn/courses/30/lessons/136798

def solution(number, limit, power):
    answer = []
    count = 0
    for i in range(1, number + 1):
        for y in range(1, i + 1):
            if i % y == 0:
                count += 1
            if count > limit:
                count = power
        answer.append(count)
        count = 0
    return sum(answer)


print(solution(5, 3, 2))
print(solution(10, 3, 2))
print(solution(15, 3, 2))


# print(solution(80000, 3, 2)) # 값이 커질경우 계산에 너무 오랜 시간이 소요됨 수정 필요

def solution2(number, limit, power):
    answer = 0
    for i in range(1, number + 1):  # i 는 기사의 번호
        count = 0
        for y in range(1, int(i ** (1 / 2)) + 1):  # y는 1~ 기사번호제곱근 까지 for
            if i % y == 0:  # 약수일경우 일단 1 카운트
                count += 1
                if y ** 2 != i:  # 제곱이 되는 약수라면 중복됨으로 한번만 새야하고 아니라면 2번
                    count += 1
            if count > limit:  # 계산된 무기의 파워가 리밋을 넘을경우 값은 power
                count = power
        answer += count
    return answer


print(solution2(5, 3, 2))
print(solution2(10, 3, 2))
print(solution2(15, 3, 2))
print(solution2(80000, 3, 2))  # 제곱근을 이용했기 때문에 큰수도 오랜시간이 걸리지 않음
