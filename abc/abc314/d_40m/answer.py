from collections import defaultdict

N = int(input())
S = input().strip()
Q = int(input())

alp_list = []
for s in S:
    alp_list.append([s, 0])

change = None
for i in range(1, Q+1):
    t, x, c = input().split()
    t, x = int(t), int(x)-1
    if t == 1:
        alp_list[x] = [c, i]
    elif t == 2:
        change = [i, "l"]
    else:
        change = [i, "u"]

res_list = []
for a, i in alp_list:
    if change is not None:
        if change[1] == "u":
            if i <= change[0]:
                res_list.append(a.upper())
            else:
                res_list.append(a)
        elif change[1] == "l":
            if i <= change[0]:
                res_list.append(a.lower())
            else:
                res_list.append(a)
    else:
        res_list.append(a)

print("".join(res_list))