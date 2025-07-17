N, M = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
res_set = set()
for u, v in A_lists:
    if u == v:
        res += 1
        continue
    tmp_list = sorted([u, v])
    if tuple(tmp_list) not in res_set:
        res_set.add(tuple(tmp_list))
    else:
        res += 1

print(res)