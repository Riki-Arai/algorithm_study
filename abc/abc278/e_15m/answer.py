'''
(1) HとWの制約が小さいが、単純な全探索だと当然ながらTLEになってしまう
(2) スライドをする際には毎回全探索をする必要はなく、変化があった部分だけを計算すれば2hや2wに抑えることができる
(3) lとkがともに0だった時の計算量はh*w+2h*(W-w)のイメージ。これを(H-h)回ほど繰り返す。
(4) HとWを300、hとwを10や100にしたとしても2秒以内に収まりそうなのであとは実装するだけ
'''
H, W, N, h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# (1)
# グリッド全体について
# key   : 数字
# value : その数字がグリッドに何個あるか
# を保存する
all_count = {}

for i in range(H):
    for j in range(W):
        x = A[i][j]
        all_count[x] = all_count.get(x, 0) + 1

# (5), (6)
# k ごとに処理する
for k in range(H - h + 1):

    # (6)
    # 行が変わったら、まず全グリッドの状態に戻す
    count = all_count.copy()

    # (2)
    # 最初に (k, 0) の h×w の部分を隠す
    for i in range(k, k + h):
        for j in range(0, w):
            x = A[i][j]

            count[x] -= 1

            # 見えている個数が0になったら削除
            if count[x] == 0:
                del count[x]

    # (3)
    # (k, 0) の答えを保存
    ans = [len(count)]

    # (4), (5)
    # 左から右へスライドする
    for l in range(1, W - w + 1):

        # -----------------------------
        # 左側から1列分、隠す対象から外れる
        # -----------------------------
        out_col = l - 1

        for i in range(k, k + h):
            x = A[i][out_col]

            count[x] = count.get(x, 0) + 1

        # -----------------------------
        # 右側から1列分、新たに隠す
        # -----------------------------
        in_col = l + w - 1

        for i in range(k, k + h):
            x = A[i][in_col]

            count[x] = count.get(x, 0) - 1

            # この数字が1個も見えなくなったら削除
            if count[x] == 0:
                del count[x]

        # 現在の種類数
        ans.append(len(count))

    print(*ans)