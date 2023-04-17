def hexDigit2Int(ch):

    if ch >= 'A' and ch <= 'F':
        ch = ch.upper()
        return ord(ch) - ord('A') + 10
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
