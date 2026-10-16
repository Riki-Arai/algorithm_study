'''
(1) それぞれのaに対してNGの組み合わせ以外で最大のbを選択したい
(2) Bの数列はSortedListに放り込んで常に末尾を取得すれば良いのだが、NGの組み合わせの可能性がある
(3) NGの組み合わせはせいぜい10**5であり、aごとにNGのbい一時的にに削除をし、終わったあとに追加すればいいのでは？
    → 一見するとTLEになりそうだが、常に10**5の処理をするわけではないので間に合う
(4) 逐次的な処理をしても間に合う場合もあると認識することが大事
(5) また以前にどこかでaは一つずつ見て、bは二分探索みたいな問題があったのでその類似だとも思った
'''
from sortedcontainers import SortedList
from collections import defaultdict

N, M, L = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

s_b_list = SortedList(B_list)
c2dlist_dict = defaultdict(list)
for _ in range(L):
    c, d = map(int, input().split()) # 取得例：1 2
    c2dlist_dict[c].append(d)

res = 0
for c, a in enumerate(A_list, 1):
    if c in c2dlist_dict:
        for d in c2dlist_dict[c]:
            s_b_list.discard(B_list[d-1])
        if len(s_b_list):
            res = max(a+s_b_list[-1], res)
        for d in c2dlist_dict[c]:
            s_b_list.add(B_list[d-1])
    else:
        res = max(a+s_b_list[-1], res)

print(res)