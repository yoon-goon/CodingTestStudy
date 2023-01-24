# https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True) # 한개는 오름차순, 내림차순으로 한뒤 각 인덱스끼리 곱하면 최솟값
    for i in range(len(A)):
        answer += (A[i] * B[i])

    return answer


print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))
