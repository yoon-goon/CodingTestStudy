# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    answer = ""
    letter = s[0]
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(len(s)):
        if s[i] == letter:
            count1 += 1
            answer = answer + s[i]
        else:
            count2 += 1
            answer = answer + s[i]
        if count1 == count2:
            answer = answer + " "
            letter = s[i]
            count3 += 1
    return answer + str(count3)

print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))