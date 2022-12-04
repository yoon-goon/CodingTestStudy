#https://school.programmers.co.kr/learn/courses/30/lessons/12931
def solution(n):
    answer = 0
    while n > 0:
        answer += n%10  #정답값에 입력값을 10으로 나머지계산해 첫번째 자리수를 구함
        n//=10          #입력값을 10으로 몫을 구해 자리수를 변경 ex) 294 -> 29 -> 2


    return print(answer)

solution(123)
solution(987)