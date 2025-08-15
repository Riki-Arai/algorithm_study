# DFSなどでも解けるらしいが、DSUの良い勉強になった
# DSUが便利ではあるが使い勝手には気をつけないといけない
import sys, math, itertools, bisect, functools, copy, decimal
from functools import cmp_to_key
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

H, W = map(int, input().split())
S_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

count = 0
res_dict = defaultdict(tuple)
for i in range(H):
    for j in range(W):
        if S_lists[i][j] == "#":
            res_dict[(i, j)] = count
            count += 1

# 上、右上、右、右下、下、左下、左、左上
move_lists = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
dsu = DSU(count)
w_count = 0
for i in range(H):
    for j in range(W):
        if S_lists[i][j] == "#":
            for mi, mj in move_lists:
                ii = mi+i
                jj = mj+j
                if 0 <= ii < H and 0 <= jj < W and S_lists[ii][jj] == "#":
                    f = res_dict[(i, j)]
                    s = res_dict[(ii, jj)]
                    if not dsu.same(f, s):
                        dsu.merge(f, s)

print(len(list(dsu.groups())))