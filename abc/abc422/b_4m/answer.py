H, W = map(int, input().split()) # 取得例：1 2
S_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解

move_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]
for i in range(H):
    for j in range(W):
        if S_lists[i][j] == "#":
            count = 0
            for mi, mj in move_list:
                ii = i + mi
                jj = j + mj
                if 0 <= ii < H and 0 <= jj < W and S_lists[ii][jj] == "#":
                    count += 1
            if not(count == 2 or count == 4):
                print("No")
                exit()

print("Yes")