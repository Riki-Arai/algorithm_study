'''
※本番ではギリギリできなかった・・・
(1) クエリに従って処理をするタイプは先読みや逆から処理をすると良かったりする
(2) 今回のケースでは最後に変更をした文字列が重要なので逆順に処理をすると良さそう
    → よって1度決定したら二度と考慮する必要がないことがわかる
    → 従ってまだ色を塗っていないマスを最初に持っておき、色を塗った時点で削除するといった方針でもいけそう
    → うまくいければO(Q+N)程度の計算量で済んでくれる
(3) タイルの存在によっては変更をできないのでこちらをどうするかだが、先読みを使って塗っていない色候補から除外する形でいけそう
(4) 先読みと後処理を利用しつつ、色を塗っていない候補と塗ったマスの集合を管理する形をとればいけた
(5) 特に最後の処理で確定するタイプは逆順を意識すること、最初に処理対象の集合を持ってみる(r_setのこと)、0-1管理を集合で行うという発想を学べた
    → 処理対象の集合を持ち、かつうまくはまればO(Q+N)で対処できることが多いのが利点
    → 本番時は逆順まではできたが、タイルの管理を集合で行う発想がなかったので複雑な上にWA
'''
from collections import deque

N, Q = map(int, input().split())
input_lists = [[int(x), s] for x, s in (input().split() for _ in range(Q))] # 取得例:[[1,"A"], [2,"B"] ・・[5,"E"]]

r_set = set([n for n in range(1, N+1)])
for q, qq in input_lists:
    if q == 1:
        qq = int(qq)
        if qq in r_set:
            r_set.discard(qq)
        else:
            r_set.add(qq)

res_list = [None]*(N+1)
a_set = set()
dq = deque()
for q, qq in reversed(input_lists):
    if q == 1:
        qq = int(qq)
        if qq not in a_set:
            if qq in r_set:
                r_set.discard(qq)
            else:
                r_set.add(qq)
    else:
        for n in r_set:
            res_list[n] = qq
            dq.append(n)
            a_set.add(n)

        while len(dq):
            r_set.discard(dq.popleft())

for i in range(N+1):
    if res_list[i] == None:
        res_list[i] = "a"

print("".join(res_list[1:]))