# 집합 사용
# import random

# s = set()
# while True:
#     n = random.randint(1, 20)
#     s.add(n)
#     if len(s) == 10:
#         break
# #print(s)

# lst = list(s)
# for i in lst:
#     print(i, end=' ')

# 리스트 사용
    # 리스트 사용   ##    
import random

lst = list()
while True:         # 무한 반복   
    n = random.randint(1, 20)  # 1부터 20까지 정수 생성
    if not n in lst:   # 리스트에 없으면
        lst.append(n)  # 리스트에 추가 # fdjsdfj
    if len(lst) == 10:
        break
#print(s)
#print("#########") # 주석
#print('#########')    # 주석
for i in lst:
    print(i, end=' ') 

