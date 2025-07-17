H, W = map(int, input().split())
A_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]


a, b, c, d = float("INF"), 0, float("INF"), 0
w_lists = []
for i in range(H):
    for j in range(W):
        if A_lists[i][j] == "#":
            a = min(i, a)
            b = max(i, b)
            c = min(j, c)
            d = max(j, d)
        elif A_lists[i][j] == ".":
            w_lists.append([i, j])

for w_list in w_lists:
    x, y = w_list
    if a <= x <= b and c <= y <= d:
        print("No")
        exit()

print("Yes")