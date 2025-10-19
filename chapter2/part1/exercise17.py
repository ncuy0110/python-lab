Ta = float(input("Ta = "))
V = float(input("V = "))

result = 13.12 + 0.6215 * Ta - 11.37 * (V ** 0.16) + 0.3965 * Ta * (V ** 0.16)
print(result)