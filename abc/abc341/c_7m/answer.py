H, W, N = map(int, input().split())
S = input().strip()
S_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

# 上、右、下、左
move_dict = {"U":(-1, 0), "R":(0, 1), "D":(1, 0), "L":(0, -1)}
res = 0
for i in range(H):
    for j in range(W):
        ii = i
        jj = j
        if S_lists[i][j] == ".":
            for s in S:
                h, w = move_dict[s]
                ii += h
                jj += w
                if S_lists[ii][jj] == "#":
                    break
            else:
                res += 1

print(res)