import itertools as it

N = int(input()) # 数値：1
L_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
bit_lists = list(it.product([0, 1], repeat=N))
for bit_list in bit_lists:
    tmp_res = 0
    cur_i = 0.5
    for i, b in enumerate(bit_list):
        l = L_list[i]
        if b == 1:
            if cur_i < 0 and cur_i + l > 0:
                tmp_res += 1
            cur_i += l
        else:
            if cur_i > 0 and cur_i - l < 0:
                tmp_res += 1
            cur_i -= l

    res = max(tmp_res, res)

print(res)