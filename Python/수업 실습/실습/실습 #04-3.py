def hexDigit2Int(ch):

    if ch >= 'A' and ch <= 'f': # A와 소문자 f사이에 있다면 문자열이므로
        ch = ch.upper()
        return ord(ch) - ord('A') + 10
    # 값을 구하기 위해 대문자 알파벳의 시작인 A로 빼줌
    # ch가 'B'인 경우, ord(ch)는 66이고 ord('A')는 65
    # 그래서 ord(ch) - ord('A') 계산결과는 1이 나오고, 여기에 10을 더한 11이 16진수에서 'B'의 값
    elif ch >= '0' and ch <= '9':
        return int(ch)

    # if ch == 'A' or ch == 'a':
    #     return 10
    # elif ch == 'B' or ch == 'b':
    #     return 11
    # elif ch == 'C' or ch == 'c':
    #     return 12
    # elif ch == 'D' or ch == 'd':
    #     return 13
    # elif ch == 'E' or ch == 'e':
    #     return 14
    # elif ch == 'F' or ch == 'f':
    #     return 15
    # elif ch >= '0' and ch <= '9':
    #     return int(ch)


def hex2dec(numStr):
    return hexDigit2Int(numStr[0]) * 256 + hexDigit2Int(numStr[1]) * 16 + hexDigit2Int(numStr[2])


print(hex2dec('A9E'))

print(hex2dec(input()))
