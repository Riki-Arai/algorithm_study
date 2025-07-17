# 降順にソートしてBとWの中で大きいもので選び合うようにする
# Bは常にスコアを加算するが、Wはスコアを最大化できないように制御
### ただしWが常に最大化できてもMを超えることはないようにする
N, M = map(int, input().split())
B_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
W_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

B_list.sort(reverse=True)
W_list.sort(reverse=True)

res = 0
b_score, w_score = 0, 0
for i in range(N):
    b_score += B_list[i]
    if i < M:
        w_score = max(w_score, w_score + W_list[i])

    res = max(res, b_score+w_score)

print(res)

## first
#N, M = map(int, input().split())
#B_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#W_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
#
#res = 0
#w_idx = 0
#B_list.sort(reverse=True)
#W_list.sort(reverse=True)
#for i in range(N):
#    if B_list[i] > 0:
#        if w_idx < M and W_list[w_idx] > 0:
#            res += B_list[i]
#            res += W_list[w_idx]
#            w_idx += 1
#        else:
#            res += B_list[i]
#    elif B_list[i] <= 0 and w_idx < M and W_list[w_idx] > 0 and W_list[w_idx] + B_list[i] > 0:
#        if B_list[i] < W_list[w_idx]:
#            res += B_list[i]
#            res += W_list[w_idx]
#            w_idx += 1
#    else:
#        break
#
#print(res)