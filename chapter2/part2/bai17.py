s = input()
d = {"chu_cai": 0, "chu_so": 0}
for ch in s:
    if ch.isalpha():
        d["chu_cai"] += 1
    elif ch.isdigit():
        d["chu_so"] += 1
print("Số chữ cái là:", d["chu_cai"])
print("Số chữ số là:", d["chu_so"])
