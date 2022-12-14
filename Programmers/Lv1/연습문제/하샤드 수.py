# https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    answer = True
    fletter = x % 10
    sletter = int((x/10)%10)
    tletter = int((x / 100) % 10)
    foletter = int((x / 1000) % 10)
    filetter = int((x / 10000) % 10)
    if x%(fletter+sletter+tletter+foletter+filetter) == 0:
        return True

    return False

print(solution((10)))
print(solution((12)))
print(solution((11)))
print(solution((13)))
print(solution((1234)))
print(solution((10000)))