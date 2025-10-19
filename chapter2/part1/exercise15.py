C = 4.186
JOULE_PER_KWH = 2.777e6
COST_PER_KWH = 8.9

M = float(input("Nhập khối lượng nước (gram): "))
delta_T = float(input("Nhập độ thay đổi nhiệt độ (°C): "))

Q = M * C * delta_T

energy_kwh = Q / JOULE_PER_KWH

cost = energy_kwh * COST_PER_KWH

print(f"\nNăng lượng cần thiết: {Q:.2f} Joules")
print(f"Tương đương: {energy_kwh:.6f} kWh")
print(f"Chi phí đun nóng: {cost:.4f} cent")
