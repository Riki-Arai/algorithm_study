'''
(1) それぞれの素因数の最大値となる指数によって最小公倍数を構成することまでは見抜けた
(2) しかしカウントをするための考察が足りずにTLEを抜け出せなかった
(3) 表にして考察をすることでACする糸口を掴むことができたかも？？
(4) 最大値となる指数が変わるかどうかを着目する視点が足りなかった。。。
'''
from collections import defaultdict

N = int(input())

p2e_dict = defaultdict(int)
e2n_dict = defaultdict(int)
input_lists = []

for _ in range(N):
    m = int(input())
    tmp_p2e_dict = defaultdict(int)

    for _ in range(m):
        p, e = map(int, input().split())
        # 各素数 p の最大 exponent
        p2e_dict[p] = max(p2e_dict[p], e)
        # (p, e) の組が何個あるか
        e2n_dict[(p, e)] += 1
        # i 番目の数における p の exponent
        tmp_p2e_dict[p] = e

    input_lists.append(tmp_p2e_dict)

# 同じ結果になるものをまとめる
res = set()
for d in input_lists:
    # この数を 1 にしたときに、
    # LCM の exponent が変化する素数を記録
    tmp = []
    for k, v in d.items():
        # この p の最大 exponent を、この数だけが持っている
        if v == p2e_dict[k] and e2n_dict[(k, v)] == 1:
            tmp.append(k)
    # どの素数の exponent が変化したかが同じなら
    # LCM も同じ
    res.add(tuple(tmp))

print(len(res))