import random

'''
def SumOfRandInt(count):
    if count >= 5:
        return 0
    n = random.randint(1, 100)
    print(n)
    return n + SumOfRandInt(count + 1)
'''

def SumOfRandInt(count):
    if count >= 5:
        return 0
    n = random.randint(1, 100)
    n1 = SumOfRandInt(count + 1)
    print(f"n = {n} n1 = {n1}")
    print(n)
    return n + n1


#random.seed(0)
print(SumOfRandInt(0))
