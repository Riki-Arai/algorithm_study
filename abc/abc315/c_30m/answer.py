from collections import defaultdict

N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
A_lists.sort(key=lambda x: x[1], reverse=True)
f_k, f_v = A_lists[0]
s_k, s_v = A_lists[1]
if f_k == s_k:
    res = f_v+s_v//2
else:
    res = f_v+s_v

res_dict = defaultdict(int)
for k, v in A_lists:
    if k in res_dict:
        vv = res_dict[k]
        res_dict[k] = max(v, vv)
    else:
        res_dict[k] = v

res_list = sorted(list(res_dict.values()), reverse=True)
if len(res_list) >= 2:
    res = max(res_list[0]+res_list[1], res)
    print(res)
else:
    print(res)