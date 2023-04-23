t = "Hi. i am Tom. I am a boy"


def getNextPeriodPos(txt, startpos):
    if startpos >= len(txt):
        return -1
    return txt.find('.', startpos, len(txt))

def getNextLine(txt, startpos):
    if startpos >= len(txt):
        return ''
    idx = getNextPeriodPos(txt, startpos)
    if idx == -1:  # . 이 없어도 나머지 문자열을 출력하기위함
        return txt[startpos:]
    else:
        return txt[startpos:idx + 1]

def countWordsInLine(line):
    count = 0
    if line.find(' ' or '\t' or '\n'):
        count += 1
    return count

def main():
    idx = 0

    idx = getNextPeriodPos(t, idx)
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
    idx = getNextPeriodPos(t, idx + 1)  # -1
    print(idx)

    idx = 0
    cnt = 0
    s = getNextLine(t, idx)
    print(s.strip())
    cnt += (countWordsInLine(s.strip()))
    print(cnt)
    idx += len(s)
    s = getNextLine(t, idx)
    print(s.strip())
    idx += len(s)

    s = getNextLine(t, idx)
    print(s.strip())
    idx += len(s)
    s = getNextLine(t, idx)
    print(s.strip())


main()