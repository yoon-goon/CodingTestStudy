# https://school.programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x*(i+1)) # i가 0부터 시작하기 때문에 +1
    return answer

print((solution(2,5)))
print((solution(4,3)))
print((solution(-4,2)))
print((solution(0,2)))
print((solution(4,0)))