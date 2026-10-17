# 参照URL：https://github.com/Riki-Arai/algorithm_study/blob/main/abc/utils/snippet.json
import bisect as bi

N, Q = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

n_list = [0]
cum_list = [0]
cum_cum_list = [0]
for i, a in enumerate(A_list, 1):
    cum_list.append(cum_list[-1]+a)
    cum_cum_list.append(cum_cum_list[-1]+cum_list[-1])
    n_list.append(n_list[-1]+i)

for _ in range(Q):
    L, R = map(int, input().split()) # 取得例：1 2
    L -= 1
    l_i = bi.bisect_left(n_list, L)
    r_i = bi.bisect_left(n_list, R)
    if r_i == l_i:
        res = cum_list[R%(l_i+1)-1]-cum_list[L%(l_i+1)-1]
    else:
        res = cum_cum_list[r_i]-cum_cum_list[l_i]
        res += cum_list[l_i]-cum_list[n_list[l_i]-L]
        res -= cum_list[r_i]-cum_list[r_i-(n_list[r_i]-R)]
    print(res)