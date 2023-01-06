# set()은 파이썬 내장함수로 중복을 삭제하는데 사용할 수 있다.
# 두 개 뽑아서 더하기 문제에 응용 가능

answer = [1,2,2,3,4,5,5,5,5,5,6]
print(set(answer))
'''
---> {1, 2, 3, 4, 5, 6}

값이 중괄호 형식으로 나온다
'''
print(list(set(answer)))
'''
list()를 이용해 다시 대괄호로 변경 가능
'''