seen = set()
res = []
while True:
    s = input().strip()
    if s == "":
        break
    if s not in seen:
        seen.add(s)
        res.append(s)
print(" ".join(res))
