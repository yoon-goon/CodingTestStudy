# https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    answer = ''
    newanswer = ''
    for i in range(len(food)):
        x = int(food[i]/2)
        for y in range(x):
            answer = answer+str(food.index(food[i])) # food[i]의 값이 아닌 몇번째인지가 중요함으로 index 사용
    realanswer = answer + str(0)
    ''' #풀이 과정중에 사용했으나 마지막에 슬라이싱을 통해 뒤집는 방식을 사용해 의미없어짐
    for i in range(len(food)):
        x = int(food[i]/2)
        for i in range(x):
            newanswer = newanswer+str(x)
            '''
    newanswer = answer[::-1]
    return realanswer + newanswer

#print(solution([1, 3, 4, 6]))
#print(solution([1, 7, 1, 2]))
print(solution([1,3,2,3]))