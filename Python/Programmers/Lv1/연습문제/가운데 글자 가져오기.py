# https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    slen = len(s)
    dlen = int(slen / 2)  # 홀수일 경우 .5가 붙기에 정수형

    if slen % 2 == 0:  # 짝수일경우
        return s[dlen - 1:dlen + 1]  # ex) [1,2,3,4,5]의 [0:3] -> [1,2,3] 즉 0,1,2번 자리까지만

    return s[dlen]


print(solution("abcde"))
print(solution("qwer"))
print(solution("qwe"))
print(solution("qw"))
print(solution("q"))
