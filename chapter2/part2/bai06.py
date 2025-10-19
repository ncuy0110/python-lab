s = input()
u = l = 0
for c in s:
    if c.isupper():
        u += 1
    elif c.islower():
        l += 1
print("Chữ hoa:", u)
print("Chữ thường:", l)
