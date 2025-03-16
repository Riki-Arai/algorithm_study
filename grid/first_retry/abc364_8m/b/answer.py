H, W = map(int, input().split())
S_1, S_2 = map(int, input().split())
C_list = [input() for _ in range(H)]
X_list = list(input())

S_1 -= 1
S_2 -= 1
# 上、右、下、左
move_dic = {"U":(-1, 0), "R":(0, 1), "D":(1, 0), "L":(0, -1)}
for x in X_list: 
    ii = S_1 + move_dic[x][0]
    jj = S_2 + move_dic[x][1]
    if ii >= 0 and jj >= 0 and ii < H and jj < W and C_list[ii][jj] == ".":
        S_1 = ii
        S_2 = jj

print(S_1+1, S_2+1)