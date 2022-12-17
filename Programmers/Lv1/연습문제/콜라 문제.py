# https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    count = 0
    while n >= a:
        rest = int(n / a) * b
        n = rest + (n % a)
        count += rest
    return count


print(solution(2, 1, 20))
print(solution(3, 1, 20))
