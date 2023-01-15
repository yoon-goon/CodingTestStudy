# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    temp = []
    for i in range(len(commands)):
        temp.append( array[commands[i][0]:commands[i][1]+1])

        #print(temp[commands[i][2]])
    return temp


print(solution([1,5,2,6,3,7,4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))