# 0번
# 202115060 윤석진 괭이갈매기

# 1번
def getFirstOperatorIdx(expr):
    a = expr.find("+")
    b = expr.find("-")
    c = expr.find("*")
    d = expr.find("_")
    e = expr.find(" ")
    if a == -1:
        a = 100
    if b == -1:
        b = 100
    if c == -1:
        c = 100
    if d == -1:
        d = 100
    if e == -1:
        e = 100

    if d <= a and d <= b and d <= c:
        print("getFirstOperatorIdx 오류: 첫 번째 연산자 위치가 잘못됨 ", end='')
        return -1
    if e <= a and e <= b and e <= c:
        print("getFirstOperatorIdx 오류: 첫 번째 연산자 위치가 잘못됨 ", end='')
        return -1
    # print(a,b,c,d,e)
    return min(a, b, c, d, e)

    # a = expr.find("+" or "-" or "*")
    # if a == -1:
    #     print("getFirstOperatorIdx 오류: 첫 번째 연산자 위치가 잘못됨 ", end='')
    # return a


print("\n1. getFirstOperatorIdx\n")
print(getFirstOperatorIdx("22_3-4"))  # 오류 출력 후-1 반환
print(getFirstOperatorIdx("22 3-4"))  # 오류 출력 후-1 반환
print(getFirstOperatorIdx("2+33 4"))  # 1 반환
print(getFirstOperatorIdx("22+3_4"))  # 2 반환
print(getFirstOperatorIdx("2+3-4"))  # 1 반환
print(getFirstOperatorIdx("23+3*4"))  # 2 반환


# 2번

def getSecondOperatorIdx(expr):
    a = expr.find("+")
    b = expr.find("-")
    c = expr.find("*")
    d = expr.find("_")
    e = expr.find(" ")
    # print(a,b,c,d,e)
    if max(a, b, c, d, e) == e or max(a, b, c, d, e) == d:
        print("getSecondOperatorIdx 오류: 두 번째 연산자 위치가 잘못됨 ", end='')
        return -1
    else:
        return max(a, b, c, d, e)


print("\n2. getSecondOperatorIdx\n")
print(getSecondOperatorIdx("22_3-4"))  # 4 반환
print(getSecondOperatorIdx("22 3 4"))  # 오류 출력 후 -1 반환
print(getSecondOperatorIdx("22+3_4"))  # 오류 출력 후 -1 반환
print(getSecondOperatorIdx("2+3-4"))  # 3 반환
print(getSecondOperatorIdx("23+3*4"))  # 4 반환
print(getSecondOperatorIdx("23+33*4"))  # 5 반환


# 3번
def getFirstOperand(expr):
    firstidx = getFirstOperatorIdx(expr)
    if firstidx == -1:
        return -1
    else:
        if expr[:firstidx].isdigit() == False:
            print("숫자가 아님 ",end='')
            return -1
        if len(expr[:firstidx]) >= 3:
            print("오류 너무김")
            return -1
        return expr[:firstidx]





print("\n3. getFirstOperand\n")
print(getFirstOperand("2_3-4"))    # -1  반환
print(getFirstOperand("22 3 4"))   # -1  반환
print(getFirstOperand("2a+3_4"))   # 숫자 아님 오류 출력 후 -1 반환
print(getFirstOperand("234+3-4"))  # -1  반환 (첫 번째 연산자 위치 먼저 걸림)
print(getFirstOperand("2+3*4"))    # 2   반환
print(getFirstOperand("23+33*4"))  # 23  반환

# 4번

def getSecondOperand(expr):
    secondidx = getSecondOperatorIdx(expr)
    if secondidx == -1:
        return -1
    else:
        if expr[:secondidx].isdigit() == False:
            print("숫자가 아님 ",end='')
            return -1
        return expr[:secondidx]

print("\n4. getSecondOperand\n")
print(getSecondOperand("22_3-4"))    # -1
print(getSecondOperand("22 3 4"))    # -1
print(getSecondOperand("22+3_4"))    # -1
print(getSecondOperand("22+3a+4a"))   # 두 번째 피연산자 숫자 아님 오류 출력 후 -1 반환
print(getSecondOperand("2+332-4"))   # 두 번째 피연산자 길이 오류 출력 후 -1 반환
print(getSecondOperand("23+3*4"))    # 3
print(getSecondOperand("23+33*4"))   # 33


# 5번

# print("\n5. getThirdOperand\n")
# print(getThirdOperand("22-33+4a"))   # 세 번째 피연산자 숫자 아님 오류 출력 후 -1
# print(getThirdOperand("22+3/4a"))    # 세 번째 피연산자 숫자 아님 오류 출력 후 -1
# print(getThirdOperand("22+3*a"))     # 세 번째 피연산자 숫자 아님 오류 출력 후 -1
# print(getThirdOperand("23+33*345"))  # 세 번째 피연산자 길이 오류 출력 후 -1
# print(getThirdOperand("2+3-4"))      # 4
# print(getThirdOperand("23+3*43"))    # 43


# 6번

def comparePriority(op1, op2):
    if op1 == "*" or op1 == "/" or op1 == "%":
        op1 = 0
    else:
        op1 = 1
    if op2 == "*" or op2 == "/" or op2 == "%":
        op2 = 0
    else:
        op2 = 1

    if op1 == op2:
        return 0
    elif op1 < op2:
        return 1
    else:
        return -1


print("\n6. comparePriority\n")
print(comparePriority('-', '+'))  # 0
print(comparePriority('+', '-'))  # 0
print(comparePriority('+', '*'))  # -1
print(comparePriority('*', '+'))  # 1
print(comparePriority('*', '%'))  # 0
print(comparePriority('/', '%'))  # 0

# 7 번
def calc(operand1,operator,operand2):
    if operator == '+':
        print(operand1 + operand2)
        return operand1 + operand2
    if operator == '-':
        print(operand1 - operand2)
        return operand1 - operand2
    if operator == '*':
        print(operand1 * operand2)
        return operand1 * operand2
    if operator == '/':
        print(operand1 // operand2)
        return operand1 // operand2
    if operator == '%':
        print(operand1 % operand2)
        return operand1 % operand2

print("\n7. calc\n")
calc(22, '+', 23)
calc(22, '*', 23)
calc(22, '/', 23)
calc(22, '%', 23)
calc(22, '-', 23)

# 8번

# print(calcExpression("2a+3-4"))
# print(calcExpression("2+b-4"))
# print(calcExpression("2+b-c4"))
# print(calcExpression("22_3-4"))
# print(calcExpression("22 3-4"))
# print(calcExpression("22+3_4"))
# print(calcExpression("2+3-4"))
# print(calcExpression("2+3%4"))
# print(calcExpression("2*3%4"))
# print(calcExpression("23+3*4"))
# print(calcExpression("23+3*4"))
# print(calcExpression("25+25/5"))
# print(calcExpression("25+25/25"))
