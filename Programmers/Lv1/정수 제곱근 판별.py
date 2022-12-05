# https://school.programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    i = 1
    answer = -1
    while i * i < n:
        i += 1
    if (i * i) == n:  # 처음 작성 당시엔 if문을 while 안에 넣어 i**2=n 이라는 if의 조건이 상위의 while 1*1<n 조건 때문에 성립할 수 없었음
                        # 밖으로 내보내 해결
        answer = (i + 1) ** 2
    else:
        answer = -1

    return answer


print(solution(121))
print(solution(3))
