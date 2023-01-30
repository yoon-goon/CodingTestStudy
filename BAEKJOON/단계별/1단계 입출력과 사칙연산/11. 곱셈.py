# https://www.acmicpc.net/problem/2588

a = input()
b = input()

three = int(a) * int(b[2])
four = int(a) * int(b[1])
five = int(a) * int(b[0])
six = int(a) * int(b)

print(three, four, five, six, sep="\n")
