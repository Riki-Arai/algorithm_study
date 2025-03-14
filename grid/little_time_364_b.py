H, W = map(int, input().split())
S_i, S_j = map(int, input().split())
grid_list = [list(input()) for _ in range(H)]
X = input()

S_i -= 1
S_j -= 1
move_dic = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)} # Uを(1, 0)としてしまっていたために時間がかかってしまった
for x in X:
    h_m, w_m = move_dic[x]
    tmp_s_i = S_i + h_m
    tmp_s_j = S_j + w_m
    if x == "U" and tmp_s_i >= 0 and grid_list[tmp_s_i][tmp_s_j] == ".":
        S_i = tmp_s_i
        S_j = tmp_s_j
    elif x == "D" and tmp_s_i < H and grid_list[tmp_s_i][tmp_s_j] == ".":
        S_i = tmp_s_i
        S_j = tmp_s_j
    elif x == "R" and tmp_s_j < W and grid_list[tmp_s_i][tmp_s_j] == ".":
        S_i = tmp_s_i
        S_j = tmp_s_j
    elif x == "L" and tmp_s_j >= 0 and grid_list[tmp_s_i][tmp_s_j] == ".":
        S_i = tmp_s_i
        S_j = tmp_s_j

print(S_i+1, S_j+1)

##### 以下の方法でも解ける
#H, W = map(int, input().split())
#S_i, S_j = map(int, input().split())
#grid_list = [list(input()) for _ in range(H)]
#X = input()
#
#S_i -= 1
#S_j -= 1
#move_dic = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)} # Uを(1, 0)としてしまっていたために時間がかかってしまった
#for x in X:
#    h_m, w_m = move_dic[x]
#    tmp_s_i = S_i + h_m
#    tmp_s_j = S_j + w_m
#    if tmp_s_i < H and tmp_s_i >= 0 and tmp_s_j < W and tmp_s_j >= 0 and grid_list[tmp_s_i][tmp_s_j] == ".":
#        S_i = tmp_s_i
#        S_j = tmp_s_j
#
#print(S_i+1, S_j+1)
#
