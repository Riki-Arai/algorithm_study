'''
(1) 大きい数から和の総数の公式によって求めればいい
(2) 解説や他の正解者のコードをみたがあまりいいものはなかった
'''
N, K = map(int, input().split())
A_list = list(map(int, input().split()))

# 番兵として0を追加し、降順にソート
# これにより要素数1の例外処理や、配列の最後まで到達した後の残処理が不要になります
A_list.append(0)
A_list.sort(reverse=True)

res = 0
for i in range(N):
    # 隣り合う要素が同じ場合は引く必要がないのでスキップ
    if A_list[i] == A_list[i+1]:
        continue
        
    n = (A_list[i] - A_list[i+1]) * (i + 1)
    
    if n <= K:
        # i+1個のアトラクションをすべて A_list[i+1] まで減らす
        res += (A_list[i] + A_list[i+1] + 1) * n // 2
        K -= n
    else:
        # Kが足りず、途中で回数上限に達する場合
        m, r = divmod(K, i + 1)
        res += (A_list[i] + (A_list[i] - m + 1)) * m // 2 * (i + 1)
        res += (A_list[i] - m) * r
        K = 0
        
    # 回数(K)を使い切ったら即終了
    if K == 0:
        break

print(res)