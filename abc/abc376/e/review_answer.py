'''
※GPTに実装をさせた
(1) 全探索ができれば解ける問題なのでDPを検討したが、良い情報の持ち方がなさそうなので除外
(2) Aで最大のものを選べばあとはどのAを選んでも関係がないことを踏まえると、残りのBはできる限りすくないもの選ぶといいことに気づく
(3) この方針でSortedListと優先度付きキューを用いて実装をしようとしたが、インデックス管理や削除など複雑だったのでうまく実装ができず
(4) 回答を見る限りだと実装がかなりシンプルそうなので、自分の考えからは間違えてはなかったがもっと簡単な方法に辿り着くべきだった
(5) しかし最大のものを選んでしまえば固定できて、あとはもう一つの数列については最適な選択をすればいいという考え方は有用そう
    →2つ以上の変数があるときはひとまず何か1つを固定して考えてみるという発想を常に持ってみる
'''

import heapq as hq
from sortedcontainers import SortedList

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    s_list = SortedList()
    hq_lists = []
    hq.heapify(hq_lists)

    for a, b in zip(A_list, B_list):
        hq.heappush(hq_lists, (-a, b))
        s_list.add(b)

    # A が最大の要素を1つ取り出す
    a, b = hq.heappop(hq_lists)
    s_list.discard(b)

    # 残りから B の小さい K-1 個
    sum_b = sum(s_list[:K-1])

    a *= -1
    res = a * (sum_b + b)

    while hq_lists:
        a, b = hq.heappop(hq_lists)
        a *= -1

        # 削除前に、b より小さい要素の個数を調べる
        b_i = s_list.bisect_left(b)

        s_list.discard(b)

        # b が「最小 K-1 個」の中に入っていた場合だけ更新
        if b_i < K - 1:
            sum_b -= b

            # 残りが K-1 個以上あるなら、
            # 新しく入ってくる最小の要素を加える
            if len(s_list) >= K - 1:
                sum_b += s_list[K - 2]

        # 残りから K-1 個選べないなら、
        # これ以降の候補も存在しない
        if len(s_list) < K - 1:
            break

        res = min(a * (sum_b + b), res)

    print(res)