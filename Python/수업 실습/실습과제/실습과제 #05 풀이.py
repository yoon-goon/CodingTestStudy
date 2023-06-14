# 방법 1
t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sagittis nisi at dapibus semper. Ut quis sapien vulputate, pharetra sapien vel, commodo diam. Nam tincidunt nulla sit amet neque iaculis, at interdum erat ultrices. Donec nec turpis sagittis, malesuada dui ut, pellentesque magna. Integer ultricies pharetra ex ut semper. Pellentesque ex orci, rhoncus vitae dolor in, vulputate volutpat felis. Fusce quis ornare purus."


def find(s, ss, pos):
    #    return s.find(ss, pos)
    # s1 = s[pos:]
    # for i in range(len(s1)):
    #     if s1[i] == ss:
    #         return i + pos

    for i in range(pos, len(s)):
        if s[i] == ss:
            return i
    return -1


def find(s, ss, pos):
    lenss = len(ss)
    s1 = s[pos:]
    for i in range(len(s1)):
        if s1[i:i + lenss] == ss:
            return i + pos
    return -1


def find(s, ss, pos):
    lenss = len(ss)
    for i in range(pos, len(s)):
        # if s[i:i+lenss] == ss:
        if s[i:].startswith(ss):
            return i
    return -1


def getNextPeriodPos(txt, startPos):
    if startPos >= len(txt):
        return -1
    #    return txt.find('.', startPos, len(txt))
    #    return txt.find('.', startPos)
    return find(txt, '.', startPos)


def getNextLine(txt, startPos):
    if startPos >= len(txt):
        return None
    idx = getNextPeriodPos(txt, startPos)
    if idx == -1:
        return txt[startPos:]
    else:
        return txt[startPos:idx + 1]


def main():
    idx = -1
    idx = getNextPeriodPos(t, idx + 1)
    print(idx)
    idx = getNextPeriodPos(t, idx + 1)
    print(idx)
    idx = getNextPeriodPos(t, idx + 1)
    print(idx)
    idx = getNextPeriodPos(t, idx + 1)
    print(idx)
    idx = getNextPeriodPos(t, idx + 1)
    print(idx)
    idx = getNextPeriodPos(t, idx + 1)
    print(idx)
    idx = getNextPeriodPos(t, idx + 1)
    print(idx)
    idx = getNextPeriodPos(t, idx + 1)
    print(idx)

    idx = 0
    s = getNextLine(t, idx)
    print(s)
    idx += len(s)
    s = getNextLine(t, idx)
    print(s)
    idx += len(s)
    s = getNextLine(t, idx)
    print(s)
    idx += len(s)
    s = getNextLine(t, idx)
    print(s)
    idx += len(s)
    s = getNextLine(t, idx)
    print(s)
    idx += len(s)
    s = getNextLine(t, idx)
    print(s)
    idx += len(s)
    s = getNextLine(t, idx)
    print(s)
    idx += len(s)
    s = getNextLine(t, idx)
    print(s)


main()
