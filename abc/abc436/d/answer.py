import bisect as bi
from collections import defaultdict

N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

i_dict, j_dict, k_dict = defaultdict(list), defaultdict(list), defaultdict(list)
for i in range(N):
    a = A_list[i]
    if a%7 == 0:
        i_dict[a].append(i)
    if a%5 == 0:
        j_dict[a].append(i)
    if a%3 == 0:
        k_dict[a].append(i)

res = 0
for k, v in j_dict.items():
    d = k//5
    ii = 7*d
    kk = 3*d
    ii_idx_list = i_dict[ii]
    kk_idx_list = k_dict[kk]
    if len(ii_idx_list) == 0 or len(kk_idx_list) == 0:
        continue

    for j_idx in v:
        b_ii = bi.bisect_left(ii_idx_list, j_idx)
        b_kk = bi.bisect_left(kk_idx_list, j_idx)
        res += b_ii*b_kk
        res += (len(ii_idx_list)-b_ii)*(len(kk_idx_list)-b_kk)

print(res)