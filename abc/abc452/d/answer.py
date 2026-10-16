'''
※解説AC
原因
(1) 部分列をカウントした方がわかりやすい
(2) 部分文字列の中に部分列がどれだけあるかという設定が今の自分には難しい
    →新しいTが作られるまでは、部分列の起点(T[0])となる一番左側インデックスを持ち続ける発想がなかった
    →上記をやっておけばfor文を回すたびに右側に伸ばした時のカウントができる
    →一方で新しいTを作ったあとでもインデックスを更新すれば左側に伸ばした時のカウントもしてくれる
(3) 新しいTが作られた時に左側に伸ばした時のカウント方法が新鮮だったので、この方法はぜひ使いこなせるようにしたい
'''
S = input().strip()
T = input().strip()

res = (1 + len(S)) * len(S) // 2
# 入力1を例にして考える
# dp_list[0]であればaが成立するための一番左側のインデックス
# dp_list[1]であればabが成立するための一番左側の起点(a)のインデックス
# dp_list[2]であればabaが成立するための一番左側の起点(a)のインデックス
dp_list = [-float("INF")]*len(T)
for i in range(len(S)):
    s = S[i]
    for j in range(len(T)-1, -1, -1):
        t = T[j]
        if s == t:
            if j == 0:
                dp_list[j] = max(i, dp_list[j])
            else:
                dp_list[j] = max(dp_list[j-1], dp_list[j])

    if dp_list[-1] != -float("INF"):
        res -= dp_list[-1]+1

print(res)