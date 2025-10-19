def format_words(words):
    if not words:
        return ""
    if len(words) == 1:
        return words[0]
    return ", ".join(words[:-1]) + " and " + words[-1]


a = []
while True:
    s = input().strip()
    if s == "":
        break
    a.append(s)
print(format_words(a))
