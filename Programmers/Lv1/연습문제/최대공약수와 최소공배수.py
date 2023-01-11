# https://school.programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []
    arr1 = []
    arr2 = []
    large = []  # n,m중 큰수를 할당할것
    mult = n * m  # 배수를 할당할것
    for i in range(1, n + 1):  # 공약수를 구하는 과정
        if n % i == 0:
            arr1.append(i)
    for y in range(1, m + 1):
        if m % y == 0:
            arr2.append(y)
    for x in arr1:
        if x in arr2:
            large.append(x)
    answer.append(max(large))

    for i in range(1, mult + 1):  # 공배수를 구하는 과정
        if i % n == 0 and i % m == 0:
            answer.append(i)
            return answer
    return answer


def better_sol(n, m):  # 개선 풀이
    answer = []
    smaller = min(n, m)
    multmax = n * m

    for i in range(smaller, 0, -1):  # 최대공약수
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break

    for y in range(1, multmax + 1):  # 최소공배수
        if y % n == 0 and y % m == 0:
            answer.append(y)
            break
    return answer


print(solution(3, 12))
print(better_sol(10, 20))
