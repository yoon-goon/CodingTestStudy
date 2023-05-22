def readFile(fileName):
    with open(fileName) as f:
        return f.readlines()


lst1 = readFile("MP09Data1.txt")
lst2 = readFile("MP09Data2.txt")

print(lst1, lst2)
