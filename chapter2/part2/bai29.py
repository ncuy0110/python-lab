a = float(input())
b = float(input())
c = float(input())
if a + b <= c or a + c <= b or b + c <= a:
    print("Không phải tam giác")
elif a == b == c:
    print("Đều")
elif a == b or b == c or a == c:
    print("Cân")
else:
    print("Thường")
