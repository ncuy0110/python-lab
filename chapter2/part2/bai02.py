s = input()
print(
    "Chuỗi hoa"
    if s.isupper()
    else ("Chuỗi thường" if s.islower() else "Chuỗi chứa ký tự hoa và ký tự thường")
)
