N, Q = map(int, input().split())
A_list = [int(input()) for _ in range(Q)] # 取得例：[A1、A2・・・An]、N行の入力用(int型に変換)

n2idx_dict = {i:i for i in range(1, N+1)}
idx2n_dict = {i:i for i in range(1, N+1)}
for a in A_list:
    cur_idx = n2idx_dict[a]
    if cur_idx != N:
        target_idx = cur_idx+1
        target_n = idx2n_dict[target_idx]
        idx2n_dict[cur_idx], idx2n_dict[target_idx] = target_n, a
        n2idx_dict[a], n2idx_dict[target_n] = target_idx, cur_idx
    else:
        target_idx = cur_idx-1
        target_n = idx2n_dict[target_idx]
        idx2n_dict[cur_idx], idx2n_dict[target_idx] = target_n, a
        n2idx_dict[a], n2idx_dict[target_n] = target_idx, cur_idx

res_list = [None]*N
for k, v in n2idx_dict.items():
    res_list[v-1] = k

print(*res_list)