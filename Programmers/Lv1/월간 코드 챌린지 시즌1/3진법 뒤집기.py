# https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = ''
    while n >= 3:
        n, b = divmod(n, 3)  # divmod로 몫과 나머지를 동시에 구함
        answer = answer + str(b)
    answer = (answer + str(n))  # [::-1] 원래 구하기 위해선 앞뒤반전을 하는 과정을 거쳐야하지만 과정에서 한번 뒤집으라고 했기에 생략

    return int(answer, 3)


print(solution(45))
