N, K = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
i = 0
# 問題の肝だとは思うが難しくはない
A_lists.sort(key=lambda x: x[0])
for a, b in A_lists:
    # シュミレーションではいきなりKに手を加える前に手を加えた場合の条件を確認することが大事だったりする
    if K - (a-i) >= 0:
        # 以下はipadなどから図に書き起こして処理を書いていくと良い
        K = K - (a-i) + b
        res += (a-i)
        i = a
    else:
        print(res+K)
        exit()

# 現在の街の位置からお金の分だけ移動
print(res+K)