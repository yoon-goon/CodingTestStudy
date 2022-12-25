# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    count = 0
    newarr = []
    for i in range(len(t)-2):
        newarr.append(int(t[i:i+3]))
        if newarr[i] <= int(p):
            count += 1
    return count

print(solution("3141592","271"))
print(solution("500220839878","7"))

def test():
    if "500" > "007":
        return 1
