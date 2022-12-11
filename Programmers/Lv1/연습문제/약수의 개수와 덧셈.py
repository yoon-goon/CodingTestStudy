# https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):    # 13에서 17까지 ex) range(4)로 하면 0 1 2 3 까지 나옴
        count = 0                       # 초기화
        for j in range(i):              # i 즉 처음 루프에선 0에서 13까지
            if i % (j + 1) == 0:        # 0으로 나누기계산을 할 수 없어 +1
                count += 1              # 짝수 홀수를 구분할 카운트
        if count % 2 == 0:              # 짝수일경우 + 홀수일경우 -
            answer += i
        else:
            answer -= i

    return answer


print(solution(13, 17))


for i in range(4):
    print(i)
