'''
(1) パスの全探索はDFSが得意だが、頂点や制約の数的にTLEになってしまう
(2) 値が膨大になっても全探索をしたい場合を考えた時にDPが良いが、グラフの問題でDPを扱うことはあまりない
(3) しかし今回は完全グラフからいくつか枝を除外するグラフであるため、比較的単純な構成であることからDPを使えないか？
(4) 例えば枝が除外されていなければ自分以外の値を受け取る形にできるのでDPが使えるかもしれない？
(5) しかし単純なDPだとTLEになってしまう。。。
    →ただ完全グラフに一部の枝を除外という状況を生かしたい
    →そこで除外したものを除いた値の合計を受け取る形にすればいけそうなので、これで解けることができた
(6) 木構造や完全グラフなど特殊な形である時はそこがとっかりになることや、全探索をすれば解けることができそうなものはDPを検討してみることを学べた
'''

N, M, K = map(int, input().split()) # 取得例：1 2

not_con_lists = [set() for _ in range(N+1)]
for _ in range(M):
    U, V = map(int, input().split()) # 取得例：1 2
    not_con_lists[U].add(V)
    not_con_lists[V].add(U)

MOD = 998244353
dp_lists = [[0]*(N+1) for _ in range(K+1)]
dp_lists[0][1] = 1
sum_ = 1
for k in range(1, K+1):
    for i in range(1, N+1):
        if len(not_con_lists[i]):
            sub = 0
            for j in not_con_lists[i]:
                sub = (sub+dp_lists[k-1][j])%MOD
            dp_lists[k][i] = (sum_-dp_lists[k-1][i]-sub)%MOD
        else:
            dp_lists[k][i] = (sum_-dp_lists[k-1][i])%MOD

    sum_ = sum(dp_lists[k])

print(dp_lists[K][1])