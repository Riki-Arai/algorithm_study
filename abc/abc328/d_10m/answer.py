S = input().strip()

res_lists = []
res_lists.append(S[0])

for s in S[1:]:
    if len(res_lists):
        if s == "B" and res_lists[-1] == "A":
            res_lists[-1] += s
        elif s == "C" and res_lists[-1] == "AB":
            res_lists[-1] += s
        else:
            res_lists.append(s)

        if res_lists[-1] == "ABC":
            res_lists.pop()
    else:
        res_lists.append(s)

print("".join(res_lists))