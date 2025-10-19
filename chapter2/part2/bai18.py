s = input()
d = {"chu_hoa": 0, "chu_thuong": 0}
for ch in s:
    if ch.isupper():
        d["chu_hoa"] += 1
    elif ch.islower():
        d["chu_thuong"] += 1
print("Số chữ thường:", d["chu_thuong"])
print("Số chữ hoa:", d["chu_hoa"])
