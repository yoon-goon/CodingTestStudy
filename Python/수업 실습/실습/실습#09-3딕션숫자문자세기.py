s = "D:\Program Files (x86)\Python 310\python.exe"

d = {"alpha": 0, "digit": 0}

for ch in s:
    if ch.isalpha():
        d["alpha"] += 1
    elif ch.isdigit():
        d["digit"] += 1
print(d)

a = d["alpha"]
b = d["digit"]
print(f"alpha: {a}")
print(f"digit: {b}")