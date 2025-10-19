s = input()
t = "".join(c.lower() for c in s if c.isalnum())
print("Palindrom" if t == t[::-1] else "Không phải Palindrom")
