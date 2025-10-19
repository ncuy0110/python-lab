def good(p):
    if len(p) < 8:
        return False
    hasU = any(c.isupper() for c in p)
    hasL = any(c.islower() for c in p)
    hasD = any(c.isdigit() for c in p)
    return hasU and hasL and hasD


p = input()
print(good(p))
