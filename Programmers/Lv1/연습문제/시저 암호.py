# https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    a = s.lower()
    answer = []
    alphabet = "abcdefghijklmnopqrstuwxyz"
    trans= alphabet[n:] + alphabet[:n]
    for i in a:
        loc = alphabet.index(i)
        answer.append(trans[loc])

    for y in range(len(s)):
        if s[y] == s[y].upper():
            answer[y] = answer[y].upper()
    return ''.join(answer)

print(solution("AB",1))
print(solution("aB",1))
print(solution("z",1))
print(solution("a B z",4))

