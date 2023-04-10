def getSecondword(s):
    s = s.strip()
    pos1 = s.find(' ')
    pos2 = s.find('\t')
    pos3 = s.find('\n')
    # -1보다 큰 값을 반환함
    print(s)
    print(pos1, pos2, pos3)
    p1 = max(pos1, pos2, pos3) + 1
    print(p1)
    s2 = s[p1:]
    print(s2)
    pos1 = s2.find(' ')
    pos2 = s2.find('\t')
    pos3 = s2.find('\n')
    print(pos1, pos2, pos3)
    p2 = max(pos1, pos2, pos3)
    print(p2)
    if p2 == -1:
        p2 = len(s)
    else:
        p2 += p1
    print(p2)
    return s[p1:p2]


# print(getSecondword("What a beautiful day"))
print(getSecondword("Beautiful life"))
