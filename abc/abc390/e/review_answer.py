'''
(1) 全探索であれば解ける問題であり、制約条件的にDPの方向性で考えてみる 
(2) 行と列の情報はNとXだとして、値の持ち方が難しく、タプルで三つor四つをいっぺんに持つことも考えてみたが厳しい
(3) v1などの値を固定してみることに着目していくうちに独立してDPを行うことを思いつく
(4) さらに制約的に2つの変数までは全探索ができるので、残りの1つを二分探索などで決め打ちすれば良さそう
(5) 上記の方針でも問題がないが、実際にやってみるとv3の決め方に非常につまづいてそこだけで2時間近く溶かした
    → 今回の問題では閾値以内で最大の値を取るといったことがうまくできなかった
(6) GPTにバグが起きにくい方法を聞いたところ累積maxというデータの持ち方があることを知り、まさにそれをやりたかった
(7) Nの制約で2つの変数による全探索+残りの1つを二分探索や累積maxや累積和で求めるパターンを想定することを学べた
'''
N, X = map(int, input().split())

v1_dp_list = [-float("INF")] * (X + 1)
v2_dp_list = [-float("INF")] * (X + 1)
v3_dp_list = [-float("INF")] * (X + 1)

v1_dp_list[0] = 0
v2_dp_list[0] = 0
v3_dp_list[0] = 0

for _ in range(N):
    V, A, C = map(int, input().split())

    if V == 1:
        for x in range(X, C - 1, -1):
            if v1_dp_list[x - C] >= 0:
                v1_dp_list[x] = max(
                    v1_dp_list[x],
                    v1_dp_list[x - C] + A
                )

    elif V == 2:
        for x in range(X, C - 1, -1):
            if v2_dp_list[x - C] >= 0:
                v2_dp_list[x] = max(
                    v2_dp_list[x],
                    v2_dp_list[x - C] + A
                )

    else:
        for x in range(X, C - 1, -1):
            if v3_dp_list[x - C] >= 0:
                v3_dp_list[x] = max(
                    v3_dp_list[x],
                    v3_dp_list[x - C] + A
                )

max_a = 0
for i in range(X + 1):
    max_a = max(max_a, v3_dp_list[i])
    v3_dp_list[i] = max_a

res = 0
for i in range(X + 1):
    if v1_dp_list[i] < 0:
        continue

    for j in range(X - i + 1):
        if v2_dp_list[j] < 0:
            continue

        sum_c = i + j
        remain_c = X - sum_c
        res = max(
            res,
            min(
                v1_dp_list[i],
                v2_dp_list[j],
                v3_dp_list[remain_c]
            )
        )

print(res)