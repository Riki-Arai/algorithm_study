# BFSはジャンプしてくれるので加湿器のポイントをfor文で探索する必要がなかった・・・
# 多面BFSと呼ばれる方法らしい
import sys, math, itertools, bisect, functools, copy, decimal
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
from collections import defaultdict, Counter, deque
from atcoder.dsu import DSU
sys.setrecursionlimit(10**7)

H, W, D = map(int, input().split())
S_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

h_lists = []
for i in range(H):
    for j in range(W):
        if S_lists[i][j] == "H":
            h_lists.append([i, j])

move_dict = {"L":(-1, 0), "U":(0, -1), "R":(1, 0), "D":(0, 1)}
res = 0
# 今回の一番の肝で、このメモを使用せずにマンハッタン距離を使用しようとすると壁を超えた距離を導出してしまうのでおかしくなってしまう
dis_lists = [[-1]*W for _ in range(H)]
dq = deque()
for h, w in h_lists:
    res += 1
    dq.append((h, w))
    dis_lists[h][w] = 0

while len(dq):
    h, w = dq.popleft()
    if dis_lists[h][w] >= D:
        continue

    for mw, my in move_dict.values():
        hh = h + my
        ww = w + mw
        if not(0 <= hh < H and 0 <= ww < W):
            continue
        if S_lists[hh][ww] == "#" or S_lists[hh][ww] == "H":
            continue
        if dis_lists[hh][ww] == -1:
            dis_lists[hh][ww] = dis_lists[h][w] + 1
            dq.append((hh, ww))
            res += 1

print(res)