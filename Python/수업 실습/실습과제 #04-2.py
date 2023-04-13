t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sagittis nisi at dapibus semper. Ut quis sapien vulputate, pharetra sapien vel, commodo diam. Nam tincidunt nulla sit amet neque iaculis, at interdum erat ultrices. Donec nec turpis sagittis, malesuada dui ut, pellentesque magna. Integer ultricies pharetra ex ut semper. Pellentesque ex orci, rhoncus vitae dolor in, vulputate volutpat felis. Fusce quis ornare purus."


def getNextPeriodPos(txt, startPos):
    # print(txt[startPos])
    # print(txt)
    A = txt[startPos:]
    N = A.find(".")
    startPos += N
    if N == -1:
        return -1
    print(startPos)
    getNextPeriodPos(txt, startPos + 1)

    return startPos


def getNextLine(txt, startPos):
    A = txt[startPos:]
    N = A.find(".")
    if txt[startPos:N] == :
        return
    print(txt[startPos:N + 1].strip())
    print(startPos)
    startPos += N
    getNextLine(txt, startPos+1)
    return


getNextPeriodPos(t, 0)
getNextLine(t, 0)
