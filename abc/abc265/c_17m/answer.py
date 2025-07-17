H, W = map(int, input().split())
G_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

seen_lists = [[False]*W for _ in range(H)]
move_dict = {"L":(-1, 0), "U":(0, -1), "R":(1, 0), "D":(0, 1)}
cur_w, cur_h = 0, 0
seen_lists[cur_h][cur_w] = True
while True:
    mw, mh = move_dict[G_lists[cur_h][cur_w]]
    if not(0 <= cur_w+mw < W and 0 <= cur_h+mh < H):
        break
    cur_w += mw
    cur_h += mh
    if seen_lists[cur_h][cur_w]:
        print(-1)
        exit()
    else:
        seen_lists[cur_h][cur_w] = True

print(cur_h+1, cur_w+1)