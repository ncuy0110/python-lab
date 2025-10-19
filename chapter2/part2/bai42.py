def f(x):
    r = 1
    for i in range(2, x + 1):
        r *= i
    return r


n = int(input())
print(",".join(str(f(i)) for i in range(1, n + 1)))
