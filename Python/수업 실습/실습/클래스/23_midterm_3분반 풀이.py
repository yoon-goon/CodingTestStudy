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
