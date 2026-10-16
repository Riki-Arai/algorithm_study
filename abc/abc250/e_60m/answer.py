'''
(1) 集合同士が一致しているかどうかの計算量を早くすればACできる問題だとはわかった
(2) その方法がないかを調査してみたところそのような手法があることを確認
(3) 最初は順序を入れ替えてやっていたが、未来の状態を保つことになってしまう関係でうまくいかず
(4) 先頭からN個という点に着目して素直に先頭からN個確認したときのハッシュ値を保つことで対処
'''
import random
from collections import defaultdict

N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

a_h, b_h = 0, 0
a_set, b_set = set(), set()
n2h_dict = defaultdict(int)
ai2h_dict = defaultdict(int)
bi2h_dict = defaultdict(int)
i = 1
for a, b in zip(A_list, B_list):
    if a not in n2h_dict:
        n2h_dict[a] = random.getrandbits(64)
    if b not in n2h_dict:
        n2h_dict[b] = random.getrandbits(64)

    if a not in a_set:
        a_h ^= n2h_dict[a]
        a_set.add(a)
    if b not in b_set:
        b_h ^= n2h_dict[b]
        b_set.add(b)

    ai2h_dict[i] = a_h
    bi2h_dict[i] = b_h
    i += 1

Q = int(input()) # 数値：1
for i in range(Q):
    x, y = map(int, input().split()) # 取得例：1 2
    if ai2h_dict[x] == bi2h_dict[y]:
        print("Yes")
    else:
        print("No")