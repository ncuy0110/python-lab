data = "ncuy.19it1@vku.udn.vn•Sat•Jan•5•09:14:16’"
start_pos = data.find("@")
end_pos = data.find("•", start_pos)
host = data[start_pos + 1 : end_pos]
print(host)