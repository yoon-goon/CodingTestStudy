lst = ["국어", 90, "수학", 80, "영어", 95, "과학", 100, "역사", 90]

dic = {"국어": 90, "수학": 80, "영어": 95, "과학": 100, "역사": 90}


print(dic)

sum = 0

# d = { 1 : 2, False : 20, (1, 2) : "튜플" }
for k, v in dic.items():
    print(k, v)
    sum += v
avg = sum / len(dic)
print(f"평균 {avg}")