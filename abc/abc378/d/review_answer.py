import sys
sys.setrecursionlimit(10**7)

H, W, K = map(int, input().split())
S_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

move_lists = {"L":(-1, 0), "U":(0, -1), "R":(1, 0), "D":(0, 1)}.values()
res = 0
def dfs(i, j, dis):
    global res
    for mi, mj in move_lists:
        ii = i + mi
        jj = j + mj
        if 0 <= ii < H and 0 <= jj < W and S_lists[ii][jj] != "#" and (ii, jj) not in seen_set:
            seen_set.add((ii, jj))
            if dis+1 == K:
                res += 1
            else:
                dfs(ii, jj, dis+1)
            seen_set.discard((ii, jj))

for i in range(H):
    for j in range(W):
        if S_lists[i][j] == "#":
            continue
        seen_set = set()
        seen_set.add((i, j))
        dfs(i, j, 0)

print(res)