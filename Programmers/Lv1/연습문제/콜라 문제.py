# https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    count = 0
    while n >= a:
        rest = int(n / a) * b # a개당 b개를 줌으로 총 갯수 n 에서 a 를 나누고(나머지는 int로 배제)
        n = rest + (n % a) # 갯수 n은 위에서 받은 rest 에 나누고 남아있던 갯수를 더하면 됨
        count += rest # 이 과정을 반복하면서 받은 병의 갯수를 합산
    return count


print(solution(2, 1, 20))
print(solution(3, 1, 20))
