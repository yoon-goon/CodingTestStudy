t = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sagittis nisi at dapibus semper. Ut quis sapien vulputate, pharetra sapien vel, commodo diam. Nam tincidunt nulla sit amet neque iaculis, at interdum erat ultrices. Donec nec turpis sagittis, malesuada dui ut, pellentesque magna. Integer ultricies pharetra ex ut semper. Pellentesque ex orci, rhoncus vitae dolor in, vulputate volutpat felis. Fusce quis ornare purus."


def getNextPeriodPos(txt, startPos):
    print(txt[startPos])
    print(txt)
    A = txt[startPos:]
    N = A.find(".")
    startPos += N

    return startPos


def getNextLine(txt):
    return


idx = getNextPeriodPos(t, 0)
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
line = getNextLine(t)
print(line)
