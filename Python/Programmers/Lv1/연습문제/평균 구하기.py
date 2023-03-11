# https://school.programmers.co.kr/learn/courses/30/lessons/12944

def solution(arr):
    answer = 0
    n = len(arr)
    for i in range(n):
        answer += arr[i]
    return print(answer / n)


solution([1, 2, 3, 4])
solution([5, 5])

'''
간략화 풀이
def solution(arr):
    return (sum(arr) / len(arr))
    

'''
