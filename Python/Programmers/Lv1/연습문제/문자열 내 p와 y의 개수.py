# https://school.programmers.co.kr/learn/courses/30/lessons/12916?language=python3

def solution(s):
    pcount = 0
    ycount = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':# s[0] 부터 s[len(s)] 즉 끝까지 돌면서 p혹은 P가 있을경우 카운트 +1
            pcount += 1
        if s[i] == 'y' or s[i] == 'Y':
            ycount += 1
    if pcount == ycount:
        return True
    return False

print(solution("pPoooyY"))
print(solution("Pyy"))