tot = 0
cnt = 0
while True:
    inp = input()
    if inp == "done":
        break
    v = float(inp)
    tot += v
    cnt += 1
print("Average is:", tot / cnt if cnt else 0)
