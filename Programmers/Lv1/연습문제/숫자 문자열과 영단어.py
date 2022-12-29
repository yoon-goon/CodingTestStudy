# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    s = s.replace("zero", "0")
    s = s.replace("one", "1")
    s = s.replace("two", "2")
    s = s.replace("three", "3")
    s = s.replace("four", "4")
    s = s.replace("five", "5")
    s = s.replace("six", "6")
    s = s.replace("seven", "7")
    s = s.replace("eight", "8")
    s = s.replace("nine", "9")
    return int(s)


def solution2(s):  # 개선된 다른 풀이
    dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
           "eight": "8", "nine": "9"}
    for i, y in dic.items(): # items() - 사전 데이터(키와 값을 쌍)을 리턴 (dict_items)
        s = s.replace(i, y)
    return int(s)


def solution3(s): # 좀 더 간단한 풀이
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(words)):
        s = s.replace(words[i], str(i))
    return int(s)


print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution2("one4seveneight"))
print(solution2("23four5six7"))
