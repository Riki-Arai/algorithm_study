import math, itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
# 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、続いて切り上げ、切り捨て

N, M = map(int, input().split())
S_lists = [list(input()) for _ in range(N)]

res = float("INF")
for bit in itertools.product([0, 1], repeat=N):
    flag_list = [False] * M
    tmp_res = 0
    for i, b in enumerate(bit):
        if b == 1:
            tmp_res += 1
            for j, s in enumerate(S_lists[i]):
                if s == "o":
                    flag_list[j] = True

    if all(flag_list):
        res = min(tmp_res, res)

print(res)

#N, M = map(int, input().split())
#
#bit_lists = []
#for _ in range(N):
#    S = input().strip()
#    S = S.replace("x", "0")
#    S = S.replace("o", "1")
#    bit_lists.append(int(S, 2))
#
#all_cover = (1 << M) - 1
#
#ans = N + 1
#for mask in range(1 << N):
#    coverage = 0
#    count_shops = 0
#    for i in range(N):
#        if mask & (1 << i):
#            coverage |= bit_lists[i]  # 売り場 i がカバーしている味をORで集める
#            count_shops += 1
#    # もし全味カバーできていれば (coverage == all_cover) 組合せの個数を比較
#    if coverage == all_cover:
#        ans = min(ans, count_shops)
#
#print(ans)