# https://school.programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return "김서방은 " + str(i) + "에 있다"
    return


print(solution(["Jane", "Kim"]))

# index 를 사용해 개선할 수 있을것
