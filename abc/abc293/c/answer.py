# 深さ優先探索において探索した先で何かしらの理由でreturnするときや、探索し終えた時に現在位置から1つ戻るときにpopすると良さそう
H, W = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(H)]

move_lists = [(1, 0), (0, 1)]
res = 0

def dfs(i, j, used):
    global res
    val = A_lists[i][j]
    # すでに使っている値なら枝刈り
    if val in used:
        return
    # 今のマスの値を追加
    used.add(val)
    # ゴールに到達したらカウントして終了
    if i == H - 1 and j == W - 1:
        res += 1
    else:
        # 右 or 下へ再帰的に探索
        for di, dj in move_lists:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W:
                dfs(ni, nj, used)
    # 再帰から戻るときに戻す
    used.remove(val)

dfs(0, 0, set())
print(res)