n = int(input())
d = {
    3: "tam giác",
    4: "tứ giác",
    5: "ngũ giác",
    6: "lục giác",
    7: "thất giác",
    8: "bát giác",
    9: "cửu giác",
    10: "thập giác",
}
print(d[n] if 3 <= n <= 10 else "Số cạnh không hỗ trợ")
