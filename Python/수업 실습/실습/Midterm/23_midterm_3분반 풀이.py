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

def getFirstOperand(expr):
    idx1 = getFirstOperatorIdx(expr)
    if idx1 < 0:
        return -1
    numStr = expr[:idx1]
    if len(numStr) > 2 or len(numStr) < 1:
        print("getFirstOperand 오류: 첫 번째 피연산자가 너무 길거나 짧습니다")
    elif numStr.isdigit():
        return int(numStr)
    print("getFirstOperand 오류: 첫 번째 피연산자가 숫자가 아닙니다")
    return -1

print("\n3. getFirstOperand\n")
print(getFirstOperand("2_3-4"))    # -1  반환
print(getFirstOperand("22 3 4"))   # -1  반환
print(getFirstOperand("2a+3_4"))   # 숫자 아님 오류 출력 후 -1 반환
print(getFirstOperand("234+3-4"))  # -1  반환 (첫 번째 연산자 위치 먼저 걸림)
print(getFirstOperand("2+3*4"))    # 2   반환
print(getFirstOperand("23+33*4"))  # 23  반환

def getSecondOperand(expr):
    idx1 = getFirstOperatorIdx(expr)
    if idx1 < 0:
        return -1
    idx2 = getSecondOperatorIdx(expr)
    if idx2 < 0:
        return -1
    numStr = expr[idx1 + 1:idx2]
    if len(numStr) > 2 or len(numStr) < 1:
        print("getSecondOperand 오류: 두 번째 피연산자가 너무 길거나 짧습니다")
        return -1
    elif numStr.isdigit():
        return int(numStr)
    print("getSecondOperand 오류: 두 번째 피연산자가 숫자가 아닙니다")
    return -1

print("\n4. getSecondOperand\n")
print(getSecondOperand("22_3-4"))    # -1
print(getSecondOperand("22 3 4"))    # -1
print(getSecondOperand("22+3_4"))    # -1
print(getSecondOperand("22+3a+4a"))   # 두 번째 피연산자 숫자 아님 오류 출력 후 -1 반환
print(getSecondOperand("2+332-4"))   # 두 번째 피연산자 길이 오류 출력 후 -1 반환
print(getSecondOperand("23+3*4"))    # 3
print(getSecondOperand("23+33*4"))   # 33

def getThirdOperand(expr):
    idx2 = getSecondOperatorIdx(expr)
    if idx2 < 0:
        return -1
    numStr = expr[idx2 + 1:]
    if len(numStr) > 2 or len(numStr) < 1:
        print("getThirdOperand 오류: 세 번째 피연산자가 너무 길거나 짧습니다")
        return -1
    elif numStr.isdigit():
        return int(numStr)
    print("getThirdOperand 오류: 세 번째 피연산자가 숫자가 아닙니다")
    return -1

print("\n4. getThirdOperand\n")
print(getThirdOperand("22-33+4a"))   # 세 번째 피연산자 숫자 아님 오류 출력 후 -1
print(getThirdOperand("22+3/4a"))    # 세 번째 피연산자 숫자 아님 오류 출력 후 -1
print(getThirdOperand("22+3*a"))     # 세 번째 피연산자 숫자 아님 오류 출력 후 -1
print(getThirdOperand("23+33*345"))  # 세 번째 피연산자 길이 오류 출력 후 -1
print(getThirdOperand("2+3-4"))      # 4
print(getThirdOperand("23+3*43"))    # 43

def comparePriority(op1, op2):
    if op1 == '*' or op1 == '/' or op1 == '%':
        if op2 == '*' or op2 == '/' or op2 == '%':
            return 0
        elif op2 == '+' or op2 == '-':
            return 1
    else:
        if op2 == '*' or op2 == '/' or op2 == '%':
            return -1
        elif op2 == '+' or op2 == '-':
            return 0

print("\n5. comparePriority\n")
print(comparePriority('-', '+'))    # 0
print(comparePriority('+', '-'))    # 0
print(comparePriority('+', '*'))    # -1
print(comparePriority('*', '+'))    # 1
print(comparePriority('*', '%'))    # 0
print(comparePriority('/', '%'))    # 0

def calc(operand1, operator, operand2):
    if operator == '+':
        print(f"{operand1} + {operand2} = {operand1 + operand2}")
        return operand1 + operand2
    elif operator == '-':
        print(f"{operand1} - {operand2} = {operand1 - operand2}")
        return operand1 - operand2
    elif operator == '*':
        print(f"{operand1} * {operand2} = {operand1 * operand2}")
        return operand1 * operand2
    elif operator == '/':
        print(f"{operand1} / {operand2} = {operand1 // operand2}")
        return operand1 // operand2
    elif operator == '%':
        print(f"{operand1} % {operand2} = {operand1 % operand2}")
        return operand1 % operand2

print("\n6. calc\n")
calc(22, '+', 23)
calc(22, '*', 23)
calc(22, '/', 23)
calc(22, '%', 23)
calc(22, '-', 23)

def calcExpression(expr):
    print(f"expr: {expr}")
    opIdx1 = getFirstOperatorIdx(expr)
    if (opIdx1 > 0):
        operator1 = expr[opIdx1]
    else:
        return None
    operand1 = getFirstOperand(expr)
    if operand1 == -1:
        return None
    opIdx2 = getSecondOperatorIdx(expr)
    if (opIdx2 > 0):
        operator2 = expr[opIdx2]
    else:
        return None
    operand2 = getSecondOperand(expr)
    if operand2 == -1:
        return None
    operand3 = getThirdOperand(expr)
    if operand3 == -1:
        return None
    priority = comparePriority(operator1, operator2)
    if priority >= 0:
        result = calc(operand1, operator1, operand2)
        result = calc(result, operator2, operand3)
    else:
        result = calc(operand2, operator2, operand3)
        result = calc(operand1, operator1, result)
    return result


print(calcExpression("2a+3-4"))
print(calcExpression("2+b-4"))
print(calcExpression("2+b-c4"))
print(calcExpression("22_3-4"))
print(calcExpression("22 3-4"))
print(calcExpression("22+3_4"))
print(calcExpression("2+3-4"))
print(calcExpression("2+3%4"))
print(calcExpression("2*3%4"))
print(calcExpression("23+3*4"))
print(calcExpression("23+3*4"))
print(calcExpression("25+25/5"))
print(calcExpression("25+25/25"))

