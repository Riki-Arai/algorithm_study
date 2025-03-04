S = input()
S_list = list(S)

alp_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
res = 0
cur_idx = 0
for x in alp_list:
    if x == "A":
        cur_idx = S_list.index(x) + 1
    else:
        new_idx = S_list.index(x) + 1
        dis = abs(new_idx - cur_idx)
        res += dis
        cur_idx = new_idx

print(res)
