N, R, C = map(int, input().split()) # 取得例：1 2
S = input().strip() # 取得例："A"

res_list = []
smoke_sets = set([(0, 0)])
h, w = 0, 0
for s in S:
    if s == "N":
        h += 1
        R += 1
    elif s == "E":
        w -= 1
        C -= 1
    elif s == "W":
        w += 1
        C += 1
    else:
        h -= 1
        R -= 1

    smoke_sets.add((h, w))
    if (R, C) in smoke_sets:
        res_list.append("1")
    else:
        res_list.append("0")

print("".join(res_list))