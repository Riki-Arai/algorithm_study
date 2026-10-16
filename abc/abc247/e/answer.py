from collections import deque
#  詳細：https://atcoder.github.io/ac-library/production/document_ja/segtree.html?utm_source=chatgpt.com
#  定義例(最大値)：def f(a, b): return max(a, b) seg = SegTree(f, -float('INF'), n_list)
#  使用例1：seg.prod(L-1, R)→Lは-1する, seg.get(i-1)→0-baseのインデックス
#  使用例2：区間更新はseg.set(2, 2)、区間加算はseg.set(2, seg.get(2) + 10)
from atcoder.segtree import SegTree # 単位元→和：0、乗算：1、最大：-float('INF'), 最小：float('INF')、GCD：0、LCM：1、OR：0、XOR：0、AND：(1<<60)-1(bit数が不足していれば増やす)

N, X, Y = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

def f(a, b):
    return max(a, b)

def g(a, b):
    return min(a, b)

res = 0
cur_min_l, cur_max_l = 0, 0
a_max, a_min = A_list[0], A_list[0]
dq_min, dq_max = deque(), deque()
seg_max, seg_min = SegTree(f, -float('INF'), A_list), SegTree(g, float('INF'), A_list)
for r in range(1, N):
    dq_min.append((r, A_list[r]))
    dq_max.append((r, A_list[r]))
    a_min = seg_min.prod(cur_min_l, r+1)
    a_max = seg_max.prod(cur_max_l, r+1)
    while len(dq_min) and a_min < Y:
        cur_min_l, a = dq_min.popleft()
        a_min = seg_min.prod(cur_min_l, r+1)

    while len(dq_max) and a_max > X:
        cur_max_l, a = dq_max.popleft()
        a_max = seg_min.prod(cur_max_l, r+1)

    if a_max == X and a_min == Y and len(dq_min) and len(dq_max):
        op = abs(dq_min[0][0]-dq_max[0][0])+1 + abs(dq_min[-1][0]-dq_max[-1][0])+1
        res += op*(op-1)//2

print(res)