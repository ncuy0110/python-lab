s = input()
a = [int(x) for x in s.split(",") if x.strip() != ""]
b = [x for x in a if x % 3 == 1]
print(",".join(str(x) for x in b))
