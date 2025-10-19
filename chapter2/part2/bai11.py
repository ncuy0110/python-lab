a = []
while True:
    s = input()
    if s == "done":
        break
    a.append(float(s))
print(sum(a) / len(a) if a else 0)
print(a)
