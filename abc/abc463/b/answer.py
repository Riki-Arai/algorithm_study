N, X = input().split() # 取得例："A" "B"
N = int(N)

a2n_list = ["A", "B", "C", "D", "E"]
S_lists =  [list(input()) for _ in range(N)] 

j = a2n_list.index(X)
for i in range(N):
    if S_lists[i][j] == "o":
        print("Yes")
        exit()

print("No")