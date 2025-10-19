def longer(a, b):
    if len(a) > len(b):
        print(a)
    elif len(b) > len(a):
        print(b)
    else:
        print(a)
        print(b)


s1 = input()
s2 = input()
longer(s1, s2)
