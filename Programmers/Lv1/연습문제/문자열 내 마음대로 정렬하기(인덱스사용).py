# https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    arr = []
    answer = []
    for i in strings:
        arr.append(i[n] + i)  # 각 문자 앞자리에 인덱스n에 해당하는 알파벳을 추가해 정렬에 사용
    arr.sort()
    for i in arr:
        answer.append(i[1:])  # sort()를 이용해 정렬 후 다시 맨앞 알파벳을 빼는 과정

    return answer


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))
