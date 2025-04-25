N = int(input())
A_lists = [["*"]*N for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

for i in range(N):
    j = N - i
    if i > j:
        continue
    else:
        if i % 2 == 0:
            for k in range(i, j):
                for l in range(i, j):
                    A_lists[k][l] = "#"
        else:
            for k in range(i, j):
                for l in range(i, j):
                    A_lists[k][l] = "."

for A_list in A_lists:
    print("".join(A_list))