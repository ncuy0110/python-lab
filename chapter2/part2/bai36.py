a = []
while True:
    s = input()
    if s == "0":
        break
    a.append(int(s))
a.sort()
for x in a:
    print(x)
