# https://dojang.io/mod/page/view.php?id=2398
# 문자열 다루기 기본 문제 해결에 사용됨
'''
예외 처리 사용하기
예외(exception)란 코드를 실행하는 중에 발생한 에러

try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드

'''

try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print(y)
except:  # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.')
'''
0이나 int가 아닌 자료형이 들어갈 경우 에러가 발생해 try except 없인 실행할 수 없지만
에러 발생시 except에서 처리해줌
'''
