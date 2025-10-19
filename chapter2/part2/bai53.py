def sublists(lst):
    res = [[]]
    for x in lst:
        res += [s + [x] for s in res]
    return res


lst = input().strip()
a = [int(x) for x in lst.split()] if lst else []
print(sublists(a))
