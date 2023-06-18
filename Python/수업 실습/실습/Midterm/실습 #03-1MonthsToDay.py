'''
사용자로부터 월(month)을 영어 단어로 입력 받고
해당 월이 몇 일까지 있는지 화면에 출력하는 프로
그램을 작성하라
 월의 이름은 첫 글자만 대문자로 쓰도록 함
 월 이름은 대문자와 소문자를 구별함
 예: January, February
 단 월은 1-4월까지만 처리함
 윤년은 계산하지 않음 (2월은 무조건 28일)
 1-4월과 다른 달이 입력되면 아무것도 하지 않음
1월은 31
2월 28
3월 31
4   30
5   31
6   30
7   31
8   31
9   30
10  31
11  30
12  31
'''

month = str(input())
if month == "January" :
    print("January는 31일까지있습니다.")
elif month == "Feburary":
    print("Feburary 28일까지있습니다.")
elif month == "March":
    print("march 31일까지있습니다.")
elif month == "April":
    print("April 30일까지있습니다.")


