# https://school.programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):  # 시간 초과
    answer = []
    count = 0
    for i in range(1, n + 1):
        for y in range(1, i, 1):
            if i % y == 0:
                count += 1
            if count >= 2:
                break  # break는 반복문을 끝냄
        if count == 1:
            answer.append(i)
        count = 0

    return len(answer)


def solution2(n):
    answer = []

    for i in range(2, n + 1):
        #if i == 1: continue  # continue 는 아래부분을 실행하지 않고 넘김 /
        # i를 2부터 시작해도 되고 if i == 1: continue로 생략을 해도 됨
        count = 0

        for y in range(2, int(i ** (1 / 2)) + 1):
            if i % y == 0:
                count = 1
                break

        if count == 0:
            answer.append(i)
        count = 0

    return len(answer)


print(solution2(10))
# print(solution2(7))
# print(solution2(5))
