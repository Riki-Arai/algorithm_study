S = input().lower()
ICT = "ict"

idx = 0
for s in S:
    if s == ICT[idx]:
        idx += 1
    if idx == 3:
        print("YES")
        break
else:
    print("NO")
