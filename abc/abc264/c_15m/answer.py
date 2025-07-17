import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

H, W = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(H)] # 取得例:[[1,2], [3,4]・・[9,10]]
H_1, W_2 = map(int, input().split())
B_lists = [list(map(int, input().split())) for _ in range(H_1)] # 取得例:[[1,2], [3,4]・・[9,10]]

p_h_lists = list(itertools.product([0, 1], repeat=H))
p_w_lists = list(itertools.product([0, 1], repeat=W))
for p_h_list in p_h_lists:
    for p_w_list in p_w_lists:
        res_lists = []
        for i, ip in enumerate(p_h_list):
            tmp_list = []
            for j, jp in enumerate(p_w_list):
                if ip == 1 and jp == 1:
                    tmp_list.append(A_lists[i][j])

            if len(tmp_list) > 0:
                res_lists.append(tmp_list)

        if res_lists == B_lists:
            print("Yes")
            exit()

print("No")