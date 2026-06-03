import itertools as it

N = int(input()) # 数値
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = float("INF")
bit_lists = list(it.product([0, 1], repeat=N))
for bit_list in bit_lists:
    tmp_res = 0
    i = 0
    for k, v in it.groupby(bit_list):
        v_list = list(v)
        or_v = 0
        for _ in range(len(v_list)):
            or_v |= A_list[i]
            i += 1
        tmp_res ^= or_v

    res = min(tmp_res, res)

print(res)