'''
(1) 初めは全探索でやってしまったが計算量の見積もりが甘くてTLE
(2) MEXや0~3というように扱う値は少ないのでそこに着目
(3) mex関数の値の求め方は0(1)程度で済ませることができそう
(4) MEXを満たすインデックスは悩んだが、Eを軸にして考えることでインデックスの上下関係を考えずに済むことに気づけた
(5) 以上を踏まえて実装をしたところバグもあったりしたがACできた
(6) 3つのインデックスや文字列を扱う際には真ん中を軸にして扱うことを意識すると良さそう
'''
from collections import defaultdict

N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
S = input().strip() # 取得例："A"

xa2c_dict = defaultdict(int)
for i, s in enumerate(S):
    if s == "X":
        a = A_list[i]
        xa2c_dict[a] += 1

res = 0
ma2c_dict = defaultdict(int)
for i, s in enumerate(S):
    a = A_list[i]
    if s == "M":
        ma2c_dict[a] += 1
    elif s == "E":
        for k, v in ma2c_dict.items():
            for kk, vv in xa2c_dict.items():
                mex_set = set([k, a, kk])
                for aa in range(3):
                    if aa not in mex_set:
                       res += aa*v*vv
                       break
                else:
                    res += 3*v*vv
    elif s == "X":
        if xa2c_dict[a]-1 == 0:
            del xa2c_dict[a]
        else:
            xa2c_dict[a] -= 1

print(res)