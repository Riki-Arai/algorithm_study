H, W, N = map(int, input().split())
A_lists = [["."] * W for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

# 上、右、下、左
move_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
move_pos = 0
h, w = 0, 0
for _ in range(N):
    if A_lists[h][w] == ".":
        A_lists[h][w] = "#"
        move_pos = (move_pos + 1) % 4
        h = (h + move_list[move_pos][0]) % H
        w = (w + move_list[move_pos][1]) % W

    elif A_lists[h][w] == "#":
        A_lists[h][w] = "."
        move_pos = (move_pos - 1) % 4
        h = (h + move_list[move_pos][0]) % H
        w = (w + move_list[move_pos][1]) % W

for A_list in A_lists:
    print("".join(A_list))