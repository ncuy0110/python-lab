n = int(input())
k = int(input())
x = n
S = 0
while x > 0:
    d = x % 10
    S += d**k
    x //= 10
print(f"{n} là số Amstrong, bậc: {k}" if S == n else f"{n} không phải số Amstrong")
