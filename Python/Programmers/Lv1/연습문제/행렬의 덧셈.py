# https://school.programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    for i in range(len(arr1)):
        for y in range(len(arr1[0])):
            arr1[i][y] += arr2[i][y]

    return arr1


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
