import math

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

tong = a + b
hieu = a - b
tich = a * b

if b != 0:
    thuong = a / b
    phan_du = a % b
else:
    thuong = "Không xác định (chia cho 0)"
    phan_du = "Không xác định (chia cho 0)"

if a > 0:
    log_a = math.log10(a)
else:
    log_a = "Không xác định (a ≤ 0)"

mu = a ** b

print("\n--- Kết quả ---")
print(f"Tổng: {tong}")
print(f"Hiệu: {hieu}")
print(f"Tích: {tich}")
print(f"Thương a/b: {thuong}")
print(f"Phần dư a % b: {phan_du}")
print(f"log10(a): {log_a}")
print(f"a^b: {mu}")
