s = input()
r = ""
for ch in s:
    if ch.isalpha():
        base = "A" if ch.isupper() else "a"
        r += chr((ord(ch) - ord(base) + 3) % 26 + ord(base))
    else:
        r += ch
print(r)
