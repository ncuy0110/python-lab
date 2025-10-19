neg = []
zero = []
pos = []
while True:
    s = input().strip()
    if s == "":
        break
    v = int(s)
    (neg if v < 0 else zero if v == 0 else pos).append(v)
print(*(neg + zero + pos), sep=", ")
