# https://www.acmicpc.net/problem/15649

def dfs():
    if len(s) == M: # s의 길이가 입력값 M과 같아진다면
        print(' '.join(map(str, s)))  # .join : 매개변수로 들어온 리스트에 있는 요소를 합쳐서 하나의 문자열로 반환하는 함수
        return
    for i in range(1, N + 1):
        if i in s:  # 중복되는 숫자를 피하기 위해 i가 이미 s에 있는경우 아래를 실행하지않고 for문 continue
            continue
        s.append(i)
        dfs()
        s.pop()


N, M = map(int, input().split())
s = []

print(N, M)
dfs()
