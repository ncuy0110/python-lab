from math import sin

a = float(input("Nhap gia tri a = "))
b = float(input("Nhap gia tri b = "))
c = float(input("Nhap gia tri c = "))
A = float(input("Nhap gia tri A = "))
B = float(input("Nhap gia tri B = "))
C = float(input("Nhap gia tri C = "))

print(0.5 * a * b * sin(C))
print(0.5 * a * c * sin(B))
print(0.5 * b * c * sin(A))