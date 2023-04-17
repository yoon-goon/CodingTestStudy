import random

computer = random.randint(1,6)

human = int(input("1부터 6까지의 정수값을 입력하세요"))
if not 1 <= human <= 6:

print(f"cpu:{computer}")
print(f"Human:{human}")
