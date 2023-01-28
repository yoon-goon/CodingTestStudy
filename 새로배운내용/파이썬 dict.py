# Source: https://blog.naver.com/indra494/222886972407

# 딕셔너리는 key, value 방식
# 빠른 탐색과 사용에 용이

dic01 = {}
dic01['name'] = '김철수'
dic01['id'] = 'kim'
dic01['age'] = 20
print('dic01:', dic01)

dic02 = dict()
dic02['name'] = '유재민'
dic02['id'] = 'jaemin'
dic02['age'] = 13
print('dic02:', dic02)


# 가장 가까운 같은 글자 문제 풀이에 사용 브레이크포인트 걸어 분석


def solution2(s):  # 숫자 문자열과 영단어 풀이에 사용된 예시
    dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
           "eight": "8", "nine": "9"}
    for i, y in dic.items():
        s = s.replace(i, y)
    return int(s)


print(solution2("one4seveneight"))
print(solution2("23four5six7"))
