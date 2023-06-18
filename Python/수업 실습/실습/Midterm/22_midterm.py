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
    global count
    global a
    if a >= len(line):
        count += 1
        print("이 라인의 단어갯수",count)
        return count
    if line[a] == (' ' or '\t' or '\n'):
        count += 1
        a += 1
    elif line[a] == '.':
        count += 1
        print("이 라인의 단어갯수",count)
        return count
    else:
        a += 1

count = 0
a = 0
def main():
    idx = 0
    global count
    global a

    # idx = getNextPeriodPos(t, idx)
    # print(idx)
    # idx = getNextPeriodPos(t, idx + 1)
    # print(idx)
    # idx = getNextPeriodPos(t, idx + 1)
    # print(idx)
    # idx = getNextPeriodPos(t, idx + 1)
    # print(idx)
    # idx = getNextPeriodPos(t, idx + 1)
    # print(idx)
    # idx = getNextPeriodPos(t, idx + 1)
    # print(idx)
    # idx = getNextPeriodPos(t, idx + 1)
    # print(idx)
    # idx = getNextPeriodPos(t, idx + 1)
    # print(idx)
    # idx = getNextPeriodPos(t, idx + 1)  # -1
    # print(idx)

    idx = 0
    cnt = 0
    s = getNextLine(t, idx)
    print(s.strip())
    # print(cnt)
    countWordsInLine(s)
    countWordsInLine(s)
    countWordsInLine(s)
    idx += len(s)
    s = getNextLine(t, idx)
    print(s.strip())
    count = 0
    a = 0
    countWordsInLine(s.strip())
    countWordsInLine(s.strip())
    countWordsInLine(s.strip())
    countWordsInLine(s.strip())
    countWordsInLine(s.strip())
    countWordsInLine(s.strip())
    countWordsInLine(s.strip())
    countWordsInLine(s.strip())
    countWordsInLine(s.strip())
    idx += len(s)
    s = getNextLine(t, idx)
    print(s.strip())
    count = 0
    a = 0
    countWordsInLine(s.strip())
    countWordsInLine(s.strip())
    countWordsInLine(s.strip())
    countWordsInLine(s.strip())
    countWordsInLine(s.strip())
    countWordsInLine(s.strip())
    countWordsInLine(s.strip())
    countWordsInLine(s.strip())
    countWordsInLine(s.strip())
    countWordsInLine(s.strip())
    countWordsInLine(s.strip())




    idx += len(s)
    s = getNextLine(t, idx)
    print(s.strip())



    count = 0
    a = 0
    # countWordsInLine("Hi.")
    # countWordsInLine("Hi.")
    # countWordsInLine("Hi.")


main()


