import sys
from sortedcontainers import SortedList


def solve():
    input = sys.stdin.readline

    N = int(input())
    H = list(map(int, input().split()))

    # 現在残っている「高さ」を昇順で管理する
    # 同じ高さは1個にまとめる
    heights = SortedList()

    # blocks[h] = [left, right]
    #
    # 高さ h のブロックが
    #   left + 1 ～ right
    # の区間を担当している。
    #
    # right は「その高さを最後に更新した最新のインデックス」
    blocks = {}

    # 現在の i までを、各ブロックの高さまで満たすのに必要な水量
    water = 0

    ans = []

    for i, h in enumerate(H, 1):

        # ------------------------------------------------------------
        # 1. h 未満の高さを二分探索で全部見つける
        # ------------------------------------------------------------
        k = heights.bisect_left(h)

        # 小さい高さのブロックを順に消していく
        # SortedList の先頭側なので、ここにあるものはすべて
        # 現在の h に吸収される。
        lower = heights[:k]

        # 今回 h の高さまで引き上げる領域の幅
        width = 1

        for old_h in lower:
            left, right = blocks.pop(old_h)

            # このブロックが担当していた横幅
            w = right - left

            # いったん、このブロックを「元の高さ」まで
            # 満たしていた水量を取り除く
            water -= old_h * w

            # その区間も現在の高さ h まで引き上げる
            # ので、幅を h のブロック側へ引き継ぐ
            width += w

        # lower に入っていた高さを SortedList から削除
        del heights[:k]

        # ------------------------------------------------------------
        # 2. h と同じ高さがすでにあるか
        # ------------------------------------------------------------
        if h in blocks:
            # 同じ高さのブロックがある場合、
            # 間にあった低いブロックをすべて吸収して
            # 右端を i まで伸ばす。
            #
            # 「同じ値なら最新のインデックスを保存する」
            # という考え方がここに対応している。
            left, right = blocks[h]

            # 新しく追加した幅は、必ず right ～ i の部分
            assert width == i - right

            blocks[h][1] = i

        else:
            # --------------------------------------------------------
            # 3. h より大きいブロックが残っている場合
            # --------------------------------------------------------
            if heights:
                # h より大きいブロックのうち、
                # 一番 h に近い（＝右側にある）ブロック
                # は heights[0]
                left = blocks[heights[0]][1]
            else:
                # 左端から全部が今回のブロック
                left = 0

            # 新しい h のブロックを作る
            blocks[h] = [left, i]
            heights.add(h)

            # 実際に今回追加された幅は i - left
            assert width == i - left

        # ------------------------------------------------------------
        # 4. 今回のブロックを高さ h まで満たす
        # ------------------------------------------------------------
        water += h * width

        # water + 1 回目で次の区画に水が1だけ流れ込む
        ans.append(water + 1)

    print(*ans)


if __name__ == "__main__":
    solve()