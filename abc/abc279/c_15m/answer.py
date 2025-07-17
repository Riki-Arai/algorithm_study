import math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque

H, W = map(int, input().split())
S_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]
T_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

s_dict = defaultdict(int)
t_dict = defaultdict(int)
for j in range(W):
    s_tmp_list = []
    t_tmp_list = []
    for i in range(H):
        if S_lists[i][j] == "#":
            s_tmp_list.append(i)
        if T_lists[i][j] == "#":
            t_tmp_list.append(i)
    s_dict[tuple(s_tmp_list)] += 1
    t_dict[tuple(t_tmp_list)] += 1

for k, v in s_dict.items():
    if k not in t_dict:
        print("No")
        exit()
    if t_dict[k] != v:
        print("No")
        exit()

print("Yes")