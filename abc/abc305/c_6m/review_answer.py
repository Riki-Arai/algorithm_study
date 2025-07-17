# 最初に探索する範囲だけを求めてあげ、その次に実際にピリオドになっている箇所を求めることがポイント
# 探索する範囲の決め方については以前にやったことがあったため、スムーズに処理を書くことができた
H, W = map(int, input().split())
A_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

a, b, c, d = float("INF"), 0, float("INF"), 0
for i in range(H):
    for j in range(W):
        if A_lists[i][j] == "#":
            a = min(i, a)
            b = max(i, b)
            c = min(j, c)
            d = max(j, d)

for i in range(a, b+1):
    for j in range(c, d+1):
        if A_lists[i][j] == ".":
            print(i+1, j+1)
            exit()