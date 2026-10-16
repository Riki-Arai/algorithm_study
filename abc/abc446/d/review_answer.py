'''
(1) 全探索をしたいがそれはTLEになる、また部分列の問題はDPとの相性が良い
(2) 末尾のアルファベットをキー、値を最長の長さとした辞書を持つことを考える
(3) 左から順番に情報を加えていくことで順序を崩すことなく最大長を更新できる
(4) リストでは難しいケースが辞書だと簡単になる、列の末尾を起点にしたDPを考えることを学んだ
(5) そもそも有名な問題を簡単にしたバージョンらしいので、それを知っているとより早く解けるのかも
'''
from collections import defaultdict

N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

a2l_dict = defaultdict(int)
for a in A_list:
    if a-1 in a2l_dict:
        a2l_dict[a] = max(a2l_dict[a-1] + 1, a2l_dict[a])
    else:
        a2l_dict[a] = max(1, a2l_dict[a])

print(max(a2l_dict.values()))