'''
(1) bit全探索をできれば早いが明らかにTLEになってしまう
(2) 全探索の計算量を減らす、手戻りはなさそう(=クエリを進めた時点で常に最適なものを残せばいい）いう点からDPが相性がよいかも
(3) 管理する状態はO(H*M)となるわけだが、O(N*H*M)で見積もるとまたもやTLE
(4) 今回の最大のキモだが片方に着目して考えてみたときに、例えばあるHにおいてペアとなるMは最大のもののみを残せばいいことに気づく
    →例えばある時点でH=5のときに最大のMが10であった場合で、Mが5や8などのケースについて考える意味がない
(5) よって計算量をO(N*H)まで落とせたのであとは実装をすればいい
'''
import sys; sys.setrecursionlimit(10**7)

N, H, M = map(int, input().split()) # 取得例：1 2

res = 0
dp_list = [-float("INF")]*(H+1)
dp_list[H] = M
for _ in range(1, N+1):
    A, B = map(int, input().split()) # 取得例：1 2
    res_flag = False
    new_dp_list = [-float("INF")]*(H+1)
    for i in range(H+1):
        if i+A < H+1 and dp_list[i+A] != -float("INF"):
            new_dp_list[i] = max(dp_list[i+A], new_dp_list[i])
            res_flag = True
        if dp_list[i] != -float("INF") and dp_list[i]-B >= 0:
            new_dp_list[i] = max(dp_list[i]-B, new_dp_list[i])
            res_flag = True

    if res_flag:
        res += 1
    else:
        print(res)
        exit()
    dp_list = new_dp_list.copy()

print(res)