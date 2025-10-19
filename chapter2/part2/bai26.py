ch = input().strip().lower()
if ch in "aeiou":
    print("Nguyên âm")
elif ch == "y":
    print("Có thể là nguyên âm hoặc phụ âm")
else:
    print("Phụ âm")
