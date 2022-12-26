# https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    answer = ''
    newanswer = ''
    for i in range(len(food)):
        x = int(food[i]/2)
        for i in range(x):
            answer = answer+str(x)
            ''' #풀이 과정중에 사용했으나 마지막에 슬라이싱을 통해 뒤집는 방식을 사용해 의미없어짐
    answer = answer + str(0)
    for i in range(len(food)):
        x = int(food[i]/2)
        for i in range(x):
            newanswer = newanswer+str(x)
            '''
    newanswer = answer[::-1]
    return answer + newanswer

print(solution([1, 3, 4, 6]))