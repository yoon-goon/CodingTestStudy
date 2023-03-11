#https://school.programmers.co.kr/learn/courses/30/lessons/12928
def solution(n):
    answer = 0


    for i in range(n):
        if n % (i+1) == 0 :
            answer += (i+1)
    return print(answer)
#i+1을 이용하지 않을 경우 n을 0부터 나머지계산을 시작해 에러 발생


solution(16)


