N = int(input())
A_lists = [list(input()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]
B_lists = [list(input()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

for i in range(N):
    for j in range(N):
        if A_lists[i][j] != B_lists[i][j]:
            print(i+1, j+1)
            exit()