# 0と1しか扱わない、連続であるものも2以上は扱わない点がポイント
# 公式ではもっと楽な方法で解説していたが汎用性はDPの方が高いらしい
N = int(input())
S = input().strip()
C_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

# ある時点で0や1を選択した時点で、連続したものがすでに0or1個であるかどうかを管理
dp_lists = [[[float("INF"), float("INF")], [float("INF"), float("INF")]] for _ in range(N)]
if S[0] == "0":
    dp_lists[0][0][0] = 0
    dp_lists[0][1][0] = C_list[0]
else:
    dp_lists[0][0][0] = C_list[0]
    dp_lists[0][1][0] = 0

for i, s in enumerate(S[1:], 1):
    if s == "0":
        # 連続してはいけないので前回で1を選択したときのものから値を引いてくる。
        dp_lists[i][0][0] = dp_lists[i-1][1][0]
        # 連続したものが0回の時で前回0を選択した場合と、連続したものがすでに1個ある状態で前回1を選択した場合で比較。
        dp_lists[i][0][1] = min(dp_lists[i-1][0][0], dp_lists[i-1][1][1])
        # 連続してはいけないので前回で0を選択したときのものから値を引いてくる。1に変換するのでコストがかかる
        dp_lists[i][1][0] = dp_lists[i-1][0][0]+C_list[i]
        # 連続したものが0回の時で前回1を選択した場合と、連続したものがすでに1個ある状態で前回0を選択した場合で比較。
        dp_lists[i][1][1] = min(dp_lists[i-1][0][1]+C_list[i], dp_lists[i-1][1][0]+C_list[i])
    else:
        dp_lists[i][0][0] = dp_lists[i-1][1][0]+C_list[i]
        dp_lists[i][0][1] = min(dp_lists[i-1][0][0]+C_list[i], dp_lists[i-1][1][1]+C_list[i])
        dp_lists[i][1][0] = dp_lists[i-1][0][0]
        dp_lists[i][1][1] = min(dp_lists[i-1][0][1], dp_lists[i-1][1][0])

print(min(dp_lists[N-1][0][1], dp_lists[N-1][1][1]))