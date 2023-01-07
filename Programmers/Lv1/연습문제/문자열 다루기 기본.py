# https://school.programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    if 4 <= len(s) <= 6:
        try:
            int(s)
            return True
        except:
            return False
    return False


print(solution("a234"))
print(solution("1234"))
