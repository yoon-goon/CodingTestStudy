# https://school.programmers.co.kr/learn/courses/30/lessons/136798

def solution(number, limit, power):
    answer = []
    count = 0
    for i in range(1,number+1):
        for y in range(1,i+1):
            if i%y==0:
                count += 1
            if count > limit:
                count = power
        answer.append(count)
        count = 0
    return sum(answer)


print(solution(5,3,2))
print(solution(10,3,2))
print(solution(1,0,2))
