S = input().strip()
T = input().strip()

res_list = []
alp_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
for i in range(len(S)):
    s = S[i]
    t = T[i]
    s_idx = alp_list.index(s)
    t_idx = alp_list.index(t)
    if t_idx >= s_idx:
        res_list.append(t_idx-s_idx)
    else:
        res_list.append(t_idx+(26-s_idx))

if len(set(res_list)) == 1:
    print("Yes")
else:
    print("No")