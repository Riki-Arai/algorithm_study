N = int(input())
A_lists = [["*"]*N for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

for i in range(N):
    j = N - i # j = N - i -1としてもいいが、その場合はrange(i, j+1)としなければいけない
    if i <= j:
        if i % 2 == 0:
            for ii in range(i, j):
                for jj in range(i, j):
                    A_lists[ii][jj] = "#"
        else:
            for ii in range(i, j):
                for jj in range(i, j):
                    A_lists[ii][jj] = "."

for A_list in A_lists:
    print("".join(A_list))