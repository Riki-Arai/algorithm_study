N = int(input())
A_lists = [list(input()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

for i in range(N):
    for j in range(N):
        if i == j:
            if A_lists[i][j] != "-":
                print("incorrect")
                exit()
        else:
            if A_lists[i][j] == "W":
                if A_lists[j][i] != "L":
                    print("incorrect")
                    exit()
            elif A_lists[i][j] == "L":
                if A_lists[j][i] != "W":
                    print("incorrect")
                    exit()
            else:
                if A_lists[j][i] != "D":
                    print("incorrect")
                    exit()

print("correct")