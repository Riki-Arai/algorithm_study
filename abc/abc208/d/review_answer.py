N, M = map(int, input().split())

INF = float("INF")
dist = [[INF] * N for _ in range(N)]
for i in range(N):
    # 同じ地点なので距離0
    dist[i][i] = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    dist[A-1][B-1] = C

ans = 0
# 数式と異なり、kを一番上として探索
for k in range(N):
    # 常に全探索をすることもポイント
    for s in range(N):
        for t in range(N):
            # s -> t に行くコストと、 k経由で s->k, k->t のルートで行くコストを比較する
            # k=0の時に最短として更新し、その次のk=1でも更新がある場合はk=0と1を経由したことになる
            dist[s][t] = min(dist[s][t], dist[s][k] + dist[k][t])

            if dist[s][t] < INF:
                ans += dist[s][t]

print(ans)


N, M = map(int, input().split())

for _ in range(M):
    A, B, C = list(map(int, input().split()))
    dis_lists[A-1][B-1] = C


dis_lists = [[float("INF")]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            dis_lists[i][j] = 0

# k=0、1の時と徐々に数を増やす
for k in range(N):
    # 各kの時に全探索をするのでsとtの組み合わせ次第ではkを通過した値で更新をする
    for s in range(N):
        for t in range(N):
            # 仮にk=0の時にdis_lists[s][k]などが更新していた場合でk=1の時も更新できるのであれば0と1の地点を通過する時が最短となる
            dis_lists[s][t] = min(dis_lists[s][t], dis_lists[s][k] + dis_lists[k][t])
            if dis_lists[s][t] != float("INF"):
                res += dis_lists[s][t]

print(res)