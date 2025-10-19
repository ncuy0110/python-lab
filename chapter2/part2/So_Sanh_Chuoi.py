def printValue(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 > l2:
        print("chuỗi dài hơn:", s1)
    elif l2 > l1:
        print("chuỗi dài hơn:", s2)
    else:
        print(s1)
        print(s2)
