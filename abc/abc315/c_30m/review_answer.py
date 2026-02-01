# 最適解は必ず「全体で美味しさが最大のカップ」を含む形にできる
# ・味が異なる2種を選ぶ場合でも
# ・同じ味を2つ選ぶ場合でも
# これら双方含まれているケースであれば、最大値を固定しつつ比較できる処理をするように対応すればいい
N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
A_lists.sort(key=lambda x: x[1], reverse=True)
# 味がとにかく最大のものを1番目に愚直に選んで問題なし
f_f, f_s = A_lists[0][0], A_lists[0][1]
# 2番目以降は探索してふさわしいものを選べば良い
for i in range(1, N):
    s_f, s_s = A_lists[i][0], A_lists[i][1]
    if f_f == s_f:
        res = max(f_s + s_s//2, res)
    else:
        res = max(f_s + s_s, res)

print(res)


# 以下は愚直に解いた
# 同一種類同士のみ、異なる種類のみのどちらのパターンでも最大値を使うといった観点が大事
from collections import defaultdict

N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
A_lists.sort(key=lambda x: x[1], reverse=True)
f_k, f_v = A_lists[0]
s_k, s_v = A_lists[1]
# 同一種類の場合は、最大値を含むパターンのみを使えばいい
if f_k == s_k:
    res = f_v+s_v//2
# 異なる場合はそれでも構わない
else:
    res = f_v+s_v

# 種類が異なる場合の比較を準備
res_dict = defaultdict(int)
for k, v in A_lists:
    if k in res_dict:
        vv = res_dict[k]
        res_dict[k] = max(v, vv)
    else:
        res_dict[k] = v

res_list = sorted(list(res_dict.values()), reverse=True)
if len(res_list) >= 2:
    # 異なる種類の最大と同一種類での最大を比較（ただしf_k==s_kの場合のはなし）
    res = max(res_list[0]+res_list[1], res)
    print(res)
else:
    print(res)


## first
#N = int(input())
#A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]
#
#A_lists.sort(key=lambda x: x[1], reverse=True)
#f_f, f_s = A_lists[0][0], A_lists[0][1]
#s_f, s_s = A_lists[1][0], A_lists[1][1]
#if N == 2:
#    if f_f == s_f:
#        print(f_s + s_s//2)
#    else:
#        print(f_s + s_s)
#    exit()
#
#if s_f == f_f:
#    res = f_s + s_s//2
#    for i in range(2, N):
#        t_f, t_s = A_lists[i][0], A_lists[i][1]
#        if t_f == f_f:
#            res = max(f_s + t_s//2, res)
#        else:
#            res = max(f_s + t_s, res)
#    print(res)
#else:
#    print(f_s + s_s)