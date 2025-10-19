import random, string

L = random.randint(7, 10)
pwd = "".join(chr(random.randint(33, 126)) for _ in range(L))
print(pwd)
