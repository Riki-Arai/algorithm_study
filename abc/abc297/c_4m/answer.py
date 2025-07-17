H, W = map(int, input().split())
S_lists = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W-1):
        if S_lists[i][j] == "T" and S_lists[i][j+1] == "T":
            S_lists[i][j] = "P"
            S_lists[i][j+1] = "C"


for s_list in S_lists:
    print("".join(s_list))