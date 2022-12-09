# https://school.programmers.co.kr/learn/courses/30/lessons/12916?language=python3

def solution(s):
    pcount = 0
    ycount = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            pcount += 1
        if s[i] == 'y' or s[i] == 'Y':
            ycount += 1
    if pcount == ycount:
        return True
    return False

print(solution("pPoooyY"))
print(solution("Pyy"))