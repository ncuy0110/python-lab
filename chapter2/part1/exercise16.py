import math

g = 9.8
h = float(input("Nhập chiều cao vật rơi (m): "))
v_i = 0
v_f = math.sqrt(v_i**2 + 2 * g * h)

print(f"Vật chạm đất với tốc độ: {v_f:.2f} m/s")
