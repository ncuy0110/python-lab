op = input().strip().lower()
k = int(input())
s = input()
r = ""
for ch in s:
    if ch.isalpha():
        base = "A" if ch.isupper() else "a"
        t = (
            (ord(ch) - ord(base) + k) % 26
            if op == "encrypt"
            else (ord(ch) - ord(base) - k) % 26
        )
        r += chr(t + ord(base))
    else:
        r += ch
print(r)
