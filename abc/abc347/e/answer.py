'''
(1) クエリのたびに加算をした場合はTLE
(2) 一度追加して削除をされないときは加算対象になる性質を考えると累積和を使いたい
(3) 追加と削除をされた時のタイミングさえわかれば、累積和から答えを求めることが可能
(4) 毎回の加算や減算が難しいケースは累積和を考えてみるといいかも
'''
from collections import defaultdict

N, Q = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

seen_set = set()
a2il_dict = defaultdict(list)
res_list = [0]*(N+1)
cum_list = [0]
for i, a in enumerate(A_list):
    if a in seen_set:
        pre_i = a2il_dict[a].pop()
        res_list[a] += cum_list[i]-cum_list[pre_i]
        seen_set.discard(a)
        cum_list.append(cum_list[-1]+len(seen_set))
    else:
        seen_set.add(a)
        a2il_dict[a].append(i)
        cum_list.append(cum_list[-1]+len(seen_set))

for k, v in a2il_dict.items():
    if len(v):
        pre_i = v.pop()
        res_list[k] += cum_list[-1]-cum_list[pre_i]

print(*res_list[1:])