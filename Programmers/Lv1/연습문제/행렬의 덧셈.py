# https://school.programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        for y in range(len(arr2)):
            answer.append(arr1[i][y] + arr2[i][y])

    return answer

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))