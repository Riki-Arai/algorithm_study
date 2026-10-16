'''
(1) 末尾があるアルファベットという情報とその個数を持つことを考える
(2) リストでもいいが文字列を扱う場合は辞書の方が扱いやすい
(3) 部分列なので単純に左から情情を追加していく
(4) あとは隣り合わないように個数を更新していくだけ
'''
from collections import defaultdict

S = input().strip() # 取得例："A"

MOD = 998244353
dp_dict = defaultdict(int)
for s in S:
    dp_dict[s] = (dp_dict[s] + 1)%MOD
    dp_dict[s] = (dp_dict["a"] + dp_dict["b"] + dp_dict["c"])%MOD

print((dp_dict["a"]+dp_dict["b"]+dp_dict["c"])%MOD)