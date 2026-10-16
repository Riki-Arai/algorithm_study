'''
(1) 1度追加して削除をする、条件次第では左右を確認する処理で終わることから処理が実は軽い点が特に肝
(2) 左隣は1つ、右隣は条件次第で複数以上を確認することもある点も大事
(3) SortedList、区間の合成、償却計算量が肝
'''
from sortedcontainers import SortedList


N, Q = map(int, input().split())

# 黒く塗られている区間を (L, R) で管理
# SortedList なので L の昇順になる
res_list = SortedList()

# 残っている白マス数
res = N

for _ in range(Q):
    L, R = map(int, input().split())

    # L 以上の区間のうち、最初のものを探す
    #
    # すべての R >= 1 なので、
    # (L, 0) を使えば「L を第1キーとして」
    # 最初の位置を取得できる。
    i = res_list.bisect_left((L, 0))

    # 直前の区間が [L, R] と重なっている可能性がある
    if i > 0 and res_list[i - 1][1] >= L:
        i -= 1

    # 今回のクエリで新しく黒くなるマス数
    newly_black = R - L + 1

    # 最終的にまとめる区間
    new_L = L
    new_R = R

    # [L, R] と交差する既存区間をすべて処理
    while i < len(res_list):
        l, r = res_list[i]

        # [L, R] より右に完全に離れたら終了
        if r < L:
            i += 1
            continue

        if R < l:
            break

        # [l, r] と [L, R] の重なっている部分
        overlap_L = max(L, l)
        overlap_R = min(R, r)

        newly_black -= overlap_R - overlap_L + 1

        # 区間を統合
        new_L = min(new_L, l)
        new_R = max(new_R, r)

        # 既存区間を削除
        del res_list[i]

    # 今回新しく黒くなった分だけ白マスを減らす
    res -= newly_black

    # 統合した区間を追加
    res_list.add((new_L, new_R))

    print(res)