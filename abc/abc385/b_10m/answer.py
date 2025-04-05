H, W, X, Y = map(int, input().split())
A_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]
T = input()

X -= 1
Y -= 1
res = 0
done_list = []
# 上、右、下、左
move_dic = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
for t in T:
    hh, ww = move_dic[t]
    tmp_X = X + hh 
    tmp_Y = Y + ww
    if tmp_X >= 0 and tmp_X < H and tmp_Y >= 0 and tmp_Y < W and A_lists[tmp_X][tmp_Y] != "#":
        X += hh
        Y += ww
        if A_lists[X][Y] == "@" and (X, Y) not in done_list:
            res += 1
            done_list.append((X, Y))

print(X+1, Y+1, res)