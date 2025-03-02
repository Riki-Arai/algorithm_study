w_list, h_list  = [], []
for h in range(1, 9):
    S = input()
    for i, s in enumerate(S, 1):
        if s == "#":
            w_list.append(i)
            h_list.append(h)

res = 0
for w in range(1, 9):
    if w not in w_list:
        for h in range(1, 9):
            if h not in h_list:
                res += 1
print(res)
