R, C = map(int, input().split())
A_lists = [list(input()) for _ in range(R)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

for i in range(R):
    for j in range(C):
        for k in range(R):
            for l in range(C):
                if A_lists[i][j] not in (".", "#") and abs(k - i) + abs(l - j) <= int(A_lists[i][j]) and A_lists[k][l] == "#":
                    A_lists[k][l] = "."

        if A_lists[i][j] not in (".", "#"):
            A_lists[i][j] = "."

for A_list in A_lists:
    print("".join(A_list))