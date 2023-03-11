# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    large = []
    small = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            large.append(sizes[i][0])
            small.append(sizes[i][1])
        else:
            large.append(sizes[i][1])
            small.append(sizes[i][0])

    return max(large) * max(small)
