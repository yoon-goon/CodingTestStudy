# https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    answer = ''
    newanswer = ''
    for i in range(len(food)):
        x = int(food[i]/2)
        for i in range(x):
            answer = answer+str(x)
    answer = answer + str(0)
    for i in range(len(food)):
        x = int(food[i]/2)
        for i in range(x):
            newanswer = newanswer+str(x)
    newanswer = str(reversed(newanswer))
    return answer + newansweri

print(solution([1, 3, 4, 6]))