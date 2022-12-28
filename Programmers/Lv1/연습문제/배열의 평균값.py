# https://school.programmers.co.kr/learn/courses/30/lessons/120817

def solution(numbers):
    all = 0
    for i in numbers:
        all += i
    return all / len(numbers)


print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))
print(solution([2, 4, 6, 8]))
