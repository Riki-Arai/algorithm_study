N = int(input())
A_lists = [list(input()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

move_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for i in range(N):
    if i == 0:
        print(A_lists[i+1][0] + "".join(A_lists[i][:-1]))
    elif i == N - 1:
        print("".join(A_lists[i][1:]) + A_lists[i-1][-1])
    else:
        print(A_lists[i+1][0] + "".join(A_lists[i][1:-1]) + A_lists[i-1][-1])