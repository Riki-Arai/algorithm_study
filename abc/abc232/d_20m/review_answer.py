H, W = map(int, input().split())
C_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

move_lists = [(0, 1), (1, 0)]
res = 0
dis = 0
seen_set = set()
def dfs(i, j):
    global res, dis
    if (i, j) in seen_set:
        return
    seen_set.add((i, j))
    dis += 1
    res = max(dis, res)
    for mi, mj in move_lists:
        ii = i + mi
        jj = j + mj
        if 0 <= ii < H and 0 <= jj < W and C_lists[ii][jj] != "#":
            dfs(ii, jj)

    dis -= 1

dfs(0, 0)
print(res)
