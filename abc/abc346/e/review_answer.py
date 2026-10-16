'''
(1) imosなどで表を埋めることもしたが全てのマスを埋める場合だとTLE
(2) 上書きされてしまうことに着目し、最後の処理で決まるイメージ
(3) クエリを逆順にすれば基本的には解ける
(4) 最後の処理で決まるタイプの問題は逆順に考えると良いらしい
'''
from collections import defaultdict

H, W, M = map(int, input().split()) # 取得例：1 2
input_lists = [list(map(int, input().split())) for _ in range(M)]
input_lists.reverse()

adj_input_lists = []
seen_sets = set()
v_n, w_n = 0, 0
for t, a, x in input_lists:
    if (t, a) not in seen_sets:
        seen_sets.add((t, a))
        adj_input_lists.append((t, a, x))
        if t == 1:
            w_n += 1
        else:
            v_n += 1

adj_input_lists.reverse()
n2c_dict = defaultdict(int)
n2c_dict[0] = H*W
for t, a, x in adj_input_lists:
    if a == 0:
        continue
    if t == 1:
        n2c_dict[x] += W-v_n
        n2c_dict[0] -= W-v_n
        w_n -= 1
    else:
        n2c_dict[x] += H-w_n
        n2c_dict[0] -= H-w_n
        v_n -= 1

res_lists = []
for k, v in sorted(list(n2c_dict.items())):
    if v != 0:
        res_lists.append((k, v))

print(len(res_lists))
for k, v in res_lists:
    print(k, v)