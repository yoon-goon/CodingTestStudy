# https://school.programmers.co.kr/learn/courses/30/lessons/12935

'''
def solution(arr):
    x = min(arr)
    for i in range(len(arr)):
        if arr[i] == x:
            arr.pop(i)

    if arr == []:
        return [-1]

    return arr
'''


def solution(arr):
    x = min(arr)
    while x in arr: # 처음엔 for i in range로 작성했었으나 pop하면서 인덱스의 길이가 바뀌어버려 에러가 발생
        arr.remove(x)
    if arr == []:
        return [-1]
    return arr


print(solution([4, 3, 2, 1, 1]))
print(solution([10]))
print(solution([2, 3, 5, 8]))
