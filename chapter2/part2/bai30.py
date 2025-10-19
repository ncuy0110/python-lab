y = int(input())
print("Năm nhuận" if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0) else "Không nhuận")
