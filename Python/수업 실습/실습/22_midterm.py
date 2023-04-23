txt = "Hi. i am Tom. I am a boy"


def getNextPeriodPos(txt, startpos):
    if startpos > len(txt):
        return -1
    return txt.find('.', startpos, len(txt))

print(getNextPeriodPos(txt,0))
print(getNextPeriodPos(txt,3))
print(getNextPeriodPos(txt,13))

