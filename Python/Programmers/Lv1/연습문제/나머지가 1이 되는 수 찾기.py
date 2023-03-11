# https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    for i in range(n):
        if n % (i+1) == 1: #i+1 말고 i부터 진행하면 n%를 0으로 시작해 에러 발생 range(2,n)으로도 해결 가능
            return i+1
    return 0


print(solution(10))
print(solution(12))