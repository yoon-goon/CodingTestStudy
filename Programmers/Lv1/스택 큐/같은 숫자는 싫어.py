# https://school.programmers.co.kr/learn/courses/30/lessons/12906

'''
def solution(arr):
    answer = arr
    i = 0
    while i <= len(arr)-1:
        if arr[i] == arr[i+1]:
            answer.pop(i)
        i += 1
    return answer
'''


def solution(arr):
    answer = []
    i = 0
    while i <= len(arr) - 1:
        if arr[i] != arr[i + 1]:
            answer.append(arr[i])
        i += 1


print(solution([1, 1, 3, 3, 0, 1, 1]))
