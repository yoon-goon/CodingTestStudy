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


def solution(arr): # 코드 실행 및 채점완료 하지만 개선 가능해보임
    answer = []
    arr.append(10)
    i = 0
    while i < len(arr)-1:
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
        i += 1
    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4,4,4,3,3]))
print(solution([4,4,4,3,3,3]))