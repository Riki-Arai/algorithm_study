'''
※解説AC
(1) 全探索をしたい、MODを使用する、DPの検証をしたところ相性は良さそうとまではわかった
(2) しかし円環という問題に対してうまく対処はできなかった
    → 左隣のみと比較する方法を取っていたが、1番目とも常に比較する観点を持つべきだった
    → 最後のみで1番目と比較する処理だとうまく情報をわたせないパターンがあり、DPが使えなくなっていた
'''
N, M = map(int, input().split())

MOD = 998244353
dp_same = M
dp_diff = 0
for _ in range(1, N):
    new_same = dp_diff
    new_diff = dp_same * (M - 1) + dp_diff * (M - 2)

    dp_same = new_same % MOD
    dp_diff = new_diff % MOD

print(dp_diff)