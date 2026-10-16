'''
(1) 仮に小さい値に変更しても大きい値に変更してしまえば、小さい値に変更する処理は不要
(2) 順番を考慮する必要がないことがわかるので、大きい値から順番に変更することを考える
(3) また変更をするなら小さい値を対象にして、大きい値に変更をしていくと良い
(4) 一度変更した値は変更対象になることはないので、二分探索の際にはcur_iを用いて調整
'''
import bisect as bi
from collections import defaultdict

N, M = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split()))

c2n_dict = defaultdict(int)
for _ in range(M):
    B, C = map(int, input().split()) # 取得例：1 2
    c2n_dict[C] += B

A_list.sort()
c2n_lists = sorted(list(c2n_dict.items()), reverse=True)
res = 0
cur_i = 0
for c, n in c2n_lists:
    b_i = bi.bisect_right(A_list, c, cur_i)
    if b_i == cur_i:
        break
    res += c*min(n, b_i-cur_i)
    cur_i = min(n+cur_i, b_i)

res += sum(A_list[cur_i:])
print(res)