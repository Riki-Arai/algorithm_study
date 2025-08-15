# リストの要素の移動やswapは辞書や配列を用意することで計算量を削ることが多い印象
# i<jという制約があるのでi=1のものであれば1の値がどこのインデックスにあるかを事前にチェックしておく必要がある
# A_listとidx_listを同時に入れ替えてあげることもポイント（それで回答ができなかったりもした）
N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

idx_list = [None] * N
for i, a in enumerate(A_list):
    idx_list[a-1] = i

res_lists = []
for i in range(N):
    a = A_list[i]
    cur_idx = idx_list[a-1]
    tar_idx = idx_list[i]
    # idxと数列の並び替えを行う
    if cur_idx != tar_idx:
        # idxは先ほどのcur_idx、tar_idxに着目して並び替え
        idx_list[i], idx_list[a-1] = cur_idx, tar_idx
        # 数列はそれぞれのidxを参照したもの同士で並び替えをすれb良い
        A_list[cur_idx], A_list[tar_idx] = A_list[tar_idx], A_list[cur_idx]
        res_lists.append([cur_idx+1, tar_idx+1])

print(len(res_lists))
for res in res_lists:
    print(*res)