def f(x):
    return 1 if x == 0 else x * f(x - 1)


x = int(input())
print(f"Giai thừa của {x} là :", f(x))
