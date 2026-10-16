'''
(1) 連結成分の問題なのでDSUを用いていく
(2) 事前に分母と連結数をカウントし、そして赤色を緑色に変化させた時の連結数をそれぞれでカウントしていくことが大事
'''
from collections import deque
from atcoder.dsu import DSU
import math

H, W = map(int, input().split()) # 取得例：1 2
S_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解

den_n = 0
move_lists = {"L":(-1, 0), "U":(0, -1), "R":(1, 0), "D":(0, 1)}.values()
green_set = set()
dsu = DSU(H*W)
dq = deque()
for i in range(H):
    for j in range(W):
        c_g = i*W+j
        if S_lists[i][j] == "#":
            green_set.add(c_g)
            for mi, mj in move_lists:
                ii = i + mi
                jj = j + mj
                n_g = ii*W+jj
                if 0 <= ii < H and 0 <= jj < W and S_lists[ii][jj] == "#":
                    dsu.merge(c_g, n_g)
        else:
            den_n += 1
            dq.append((i, j))

con_n = 0
for g in dsu.groups():
    for n in g:
        if n in green_set:
            con_n += 1
            break

mol_n = 0
while len(dq):
    i, j = dq.popleft()
    c_g = i*W+j
    seen_set = set()
    for mi, mj in move_lists:
        ii = i + mi
        jj = j + mj
        n_g = ii*W+jj
        if 0 <= ii < H and 0 <= jj < W and n_g in green_set:
            seen_set.add(dsu.leader(n_g))

    if len(seen_set) >= 2:
        mol_n += con_n-(len(seen_set)-1)
    elif len(seen_set) == 1:
        mol_n += con_n
    else:
        mol_n += con_n+1

MOD = 998244353
# 割り算を期待値で出力(mol_nが分子、den_nが分母)
g = math.gcd(mol_n, den_n)
print((mol_n//g * pow(den_n//g, MOD-2, MOD)) % MOD)