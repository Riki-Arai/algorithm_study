'''
※後日AC
(1) bit全探索ができればいいがTLEになるので持つべき情報を工夫できればDPでいける問題
(2) この問題の肝としては管理するべき情報が6**5ほどで済み、N=100であるのでDPを適用することができる
(3) DPを適用するのであれば管理する情報で、処理をうまく圧縮することができるかを考えることができるかを学んだ
(4) また1次元DP的な方法を辞書でやる方法も学べた
'''
from collections import defaultdict

N, K, P = map(int, input().split()) # 取得例：1 2

pt2c_dict = defaultdict(lambda: float("INF"))
pt2c_dict[tuple([0]*K)] = 0
for _ in range(N):
    input_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
    new_pt2c_dict = defaultdict(lambda: float("INF"))
    new_pt2c_dict[tuple([0]*K)] = 0
    for k, v in pt2c_dict.items():
        k_list = list(k)
        new_pt2c_dict[tuple(k_list)] = min(v, new_pt2c_dict[tuple(k_list)]) 
        for i, a in enumerate(input_list[1:]):
            k_list[i] = min(k_list[i]+a, P)
        new_pt2c_dict[tuple(k_list)] = min(input_list[0]+v,  new_pt2c_dict[tuple(k_list)])

    pt2c_dict = new_pt2c_dict

if pt2c_dict[tuple([P]*K)] != float("INF"):
    print(pt2c_dict[tuple([P]*K)])
else:
    print(-1)