# https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    a = s.lower()
    answer = []
    alphabet = "abcdefghijklmnopqrstuwxyz" # ' ' 공백을 구현하기위해 앞에 띄어쓰기 추가
    space = " abcdefghijklmnopqrstuwxyz"
    trans= ' ' + alphabet[n+1:] + alphabet[:n+1] # 공백이 생긴만큼 abcdefghijklmnopqrstuwxyz a 로 되기때문에 +1
    print(trans)
    for i in a:
        loc = space.index(i)
        answer.append(trans[loc])

    for y in range(len(s)):
        if s[y] == s[y].upper():
            answer[y] = answer[y].upper()
    return ''.join(answer)

print(solution("AB",1))
print(solution("aB",1))
print(solution("z",1))
print(solution("a B z",4))

