def make_print():
    a = []
    for i in range(1, 21):
        a.append(i**2)
    print(a[:5] + a[-5:])


make_print()
