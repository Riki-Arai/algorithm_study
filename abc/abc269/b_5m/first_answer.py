S_lists = [list(input()) for _ in range(10)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

a, b, c, d = 100, 0, 100, 0
for i in range(10):
    for j in range(10):
        if S_lists[i][j] == "#":
            a = min(a, i)
            b = max(b, i)
            c = min(c, j)
            d = max(d, j)

print(a+1, b+1)
print(c+1, d+1)