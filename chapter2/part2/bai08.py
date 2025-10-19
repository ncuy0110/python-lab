rem = """!()-[]{};:"\,<>./?@#$%^&*_~"""
s = input()
t = ""
for ch in s:
    if ch not in rem:
        t += ch
print(t)
