def perfect(n):
    if n < 2:
        return False
    s = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            s += i
            if i * i != n:
                s += n // i
        i += 1
    return s == n


n = int(input())
print(perfect(n))
for x in range(1, 10001):
    if perfect(x):
        print(x)
