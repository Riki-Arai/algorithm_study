# 補助付きACをしたが、そもそも正攻法ではなかったっぽく、DFSを利用することが正攻法らしい
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

count = 0
def dfs(i, j, seen):
    global count
    if A[i][j] in seen:
        return
    seen.add(A[i][j])
    if i == H-1 and j == W-1:
        count += 1
        return
    if i+1 < H:
        dfs(i+1, j, seen.copy())
    if j+1 < W:
        dfs(i, j+1, seen.copy())
dfs(0, 0, set())
print(count)

#from itertools import combinations
#
#H, W = map(int, input().split())
#A_lists = [list(map(int, input().split())) for _ in range(H)]  # 例: [[1,2], [3,4]・・[9,10]]
#
#res = 0
#
#for comb in combinations(range(H + W - 2), H - 1):
#    moves = []
#    for i in range(H + W - 2):
#        if i in comb:
#            moves.append((1, 0))
#        else:
#            moves.append((0, 1))
#
#    h_idx, w_idx = 0, 0
#    res_list = [A_lists[0][0]]
#    for dh, dw in moves:
#        h_idx += dh
#        w_idx += dw
#        res_list.append(A_lists[h_idx][w_idx])
#
#    if len(set(res_list)) == len(res_list):
#        res += 1
#
#print(res)