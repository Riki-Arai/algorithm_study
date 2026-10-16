'''
(1) グリッドの矩形を扱う問題であることから二次元累積和を採用
(2) しかし正方形のみを扱う方法がわからずにいたが、正方形は全て同じ辺の長さであることに着目
(3) そこから縦と横で起点となる点から同じだけの長さを取ることで正方形を作ることができるとわかった
(4) さらにある長さ以降はFalseになる性質あるので二分探索を使える
(5) ただ二次元累積和の扱いや二分探索を久々に使ったことで変なミスもあったことで実装に時間がかかる
(6) 正方形などの縦と横で同じ長さに着目する、扱う値が非負であれば累積和は単調性を利用しやすいことが学べた
'''
import sys; sys.setrecursionlimit(10**7)

H, W, N = map(int, input().split()) # 取得例：1 2
g_lists = [[0]*W for _ in range(H)]
for _ in range(N):
    a, b = map(int, input().split()) # 取得例：1 2
    g_lists[a-1][b-1] = 1

# H: 行数, W: 列数, A: 元の2次元配列 (0-indexed前提)
# cum_lists[i][j]: 左上 (0,0) から 右下 (i-1, j-1) までの矩形和
cum_lists = [[0] * (W + 1) for _ in range(H + 1)]
for i in range(H):
    for j in range(W):
        cum_lists[i+1][j+1] = cum_lists[i+1][j] + cum_lists[i][j+1] - cum_lists[i][j] + g_lists[i][j]

def is_ok(r1, r2, c1, c2):
    if not(r2 < len(cum_lists) and c2 < len(cum_lists[r2])):
        return False
    return cum_lists[r2][c2] - cum_lists[r1 - 1][c2] - cum_lists[r2][c1 - 1] + cum_lists[r1 - 1][c1 - 1] == 0

res = 0
for r1 in range(1, H+1):
    for c1 in range(1, W+1):
        ok, ng = -1, min(H-(r1-1), W-(c1-1))+1
        while abs(ok - ng) > 1:  # 絶対値を使用しているのでok と ng の大小に関係なく、同じ条件式で良い。
            mid = (ok + ng) // 2
            # ok と ng の大小に関わらず変更なし。(参考：https://zenn.dev/forcia_tech/articles/20191223_advent_calendar)
            if is_ok(r1, r1+mid, c1, c1+mid):
                ok = mid
            else:
                ng = mid
        if ok > -1:
            res += ok+1

print(res)