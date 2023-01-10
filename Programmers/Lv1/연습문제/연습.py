def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))

a = []
for i in "122":
        if a[-1:] == [i]: continue
        a.append(i)

print(a)