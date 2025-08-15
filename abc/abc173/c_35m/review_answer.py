import sys
import itertools

input = sys.stdin.readline
H, W, K = map(int, input().split())
A = [input().strip() for _ in range(H)]

# 黒マスの座標をリスト化
black_cells = [(i, j) for i in range(H) for j in range(W) if A[i][j] == '#']
total_black = len(black_cells)

res = 0
# itertools.productを使って行・列を全探索
for row_sel in itertools.product([0, 1], repeat=H):
    for col_sel in itertools.product([0, 1], repeat=W):
        painted = 0
        # 選んだ行または列に属する黒マスをカウント
        for r, c in black_cells:
            if row_sel[r] == 1 or col_sel[c] == 1:
                painted += 1
        # 残る黒マスがK個ならカウント
        if total_black - painted == K:
            res += 1

print(res)

## first
#import sys, math, itertools, bisect, functools, copy, decimal
#from functools import cmp_to_key
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from sortedcontainers import SortedSet, SortedList, SortedDict
#from collections import defaultdict, Counter, deque
#from atcoder.dsu import DSU
#sys.setrecursionlimit(10**7)
#
#H, W, K = map(int, input().split()) # 取得例：1 2
#A_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解
#
#b_num = 0
#for i in range(H):
#    for j in range(W):
#        if A_lists[i][j] == "#":
#            b_num += 1
#
#res = 0
#h_p_lists = list(itertools.product([0, 1], repeat=H))
#w_p_lists = list(itertools.product([0, 1], repeat=W))
#for h_p_list in h_p_lists:
#    for w_p_list in w_p_lists:
#        c_A_lists = copy.deepcopy(A_lists)
#        tmp_b_num = b_num
#        for i, pi in enumerate(h_p_list):
#            if pi == 1:
#                for j in range(W):
#                    if c_A_lists[i][j] == "#":
#                        tmp_b_num -= 1
#                        c_A_lists[i][j] = "*"
#            for j, pj in enumerate(w_p_list):
#                if pj == 1:
#                    for i in range(H):
#                        if c_A_lists[i][j] == "#":
#                            tmp_b_num -= 1
#                            c_A_lists[i][j] = "*"
#        if tmp_b_num == K:
#            res += 1
#
#print(res)