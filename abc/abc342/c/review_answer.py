# あらかじめ辞書を用意するパターン
# 変換パターンごとに辞書の探索があるが、26個程度であれば計算量に問題はない
N = int(input())
S = input().strip()
Q = int(input())

# res[i] が示すのは「文字 'a' + i は最終的にどの文字に置き換わるか」
# 初期状態では自分自身に対応
res = {chr(i):chr(i) for i in range(ord('a'), ord('z') + 1)}

for _ in range(Q):
    c, d = input().split()
    if c == d:
        continue
    # 辞書のキーはSのインデックスを表現しているようなものと考えれば多少理解しやすいか？
    # 辞書の値はインデックスに対する最終的に変換したい文字列
    for k in res:
        # 値がcと同値ならdに変換することになるので更新
        if res[k] == c:
            res[k] = d

# Q回の操作をすべて反映した置換マッピングで S を変換して出力する
ans = []
for ch in S:
    ans.append(res[ch])

print("".join(ans))


#import math, itertools, bisect, functools, copy, decimal
## 天井と床関数は丸める仕様らしく、桁数が上がると期待通りの動作をしないことを確認したのでimportしていない
#from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN # 左のROUND_HALF_UPから四捨五入、四捨五入(銀行丸め)、切り上げ、切り捨て
#from collections import defaultdict, Counter, deque
#
#N = int(input())
#S = input().strip()
#Q = int(input())
#
#con_dict = {}
#con_set = set()
#for _ in range(Q):
#    A, B = input().split()
#    if A == B:
#        continue
#    if A not in con_set:
#        con_dict[A] = B
#        con_set.add(B)
#    else:
#        con_dict.pop(B, None)
#        con_set.discard(B)
#        con_dict[A] = B
#        con_set.add(A)
#
#res_dict = defaultdict(list)
#s_list = list(S)
#for i, s in enumerate(s_list):
#    res_dict[s].append(i)
#
#for k, v in con_dict.items():
#    if k in res_dict:
#        vv = res_dict[k]
#        del res_dict[k]
#        res_dict[v] = vv
#
#for k, v_list in res_dict.items():
#    for v in v_list:
#        s_list[v] = k
#
#print("".join(s_list))