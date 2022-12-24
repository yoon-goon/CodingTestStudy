# https://school.programmers.co.kr/learn/courses/30/lessons/12935


def solution(arr):
    x = min(arr)
    for i in range(len(arr)):
        if arr[i] == x:
            arr.pop(i)

    if arr == []:
        return [-1]

    return arr


print(solution([4, 3, 2, 1,1]))
print(solution([10]))
print(solution([2, 3, 5, 8]))
