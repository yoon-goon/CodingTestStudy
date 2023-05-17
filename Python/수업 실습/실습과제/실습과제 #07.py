



f = open("lorem.txt")
s = f.readline()

while s:
    print(s,end="")
    s = f.readline()
f.close()