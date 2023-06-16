def isOperator(ch):
    return ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '%'

def getFirstOperatorIdx(expr):
    if isOperator(expr[1]):
        return 1
    elif isOperator(expr[2]):
        return 2
    else:
        print("getFirstOperatorIdx 오류: 첫 번째 연산자 위치가 잘못됨")
        return -1

print("\n1. getFirstOperatorIdx\n")
print(getFirstOperatorIdx("22_3-4"))   # 오류 출력 후-1 반환
print(getFirstOperatorIdx("22 3-4"))   # 오류 출력 후-1 반환
print(getFirstOperatorIdx("2+33 4"))   # 1 반환
print(getFirstOperatorIdx("22+3_4"))   # 2 반환
print(getFirstOperatorIdx("2+3-4"))    # 1 반환
print(getFirstOperatorIdx("23+3*4"))   # 2 반환

def getSecondOperatorIdx(expr):
    if isOperator(expr[3]):
        return 3
    elif isOperator(expr[4]):
        return 4
    elif isOperator(expr[5]):
        return 5
    else: 
        print("getSecondOperatorIdx 오류: 두 번째 연산자 위치가 잘못됨")
        return -1

print("\n2. getSecondOperatorIdx\n")
print(getSecondOperatorIdx("22_3-4"))   # 4 반환
print(getSecondOperatorIdx("22 3 4"))   # 오류 출력 후 -1 반환
print(getSecondOperatorIdx("22+3_4"))   # 오류 출력 후 -1 반환
print(getSecondOperatorIdx("2+3-4"))    # 3 반환
print(getSecondOperatorIdx("23+3*4"))   # 4 반환
print(getSecondOperatorIdx("23+33*4"))  # 5 반환