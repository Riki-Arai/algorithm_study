H, W, X, Y = map(int, input().split())
row_list = [list(input()) for _ in range(H)]
col_list = [col for col in zip(*row_list)]

x_row = row_list[X-1]
y_col = col_list[Y-1]

res = 0
if x_row[Y-1] == ".":
    res += 1

for row in x_row[:Y-1][::-1]:
    if row == "#":
        break
    res += 1

for row in x_row[Y:]:
    if row == "#":
        break
    res += 1

for col in y_col[:X-1][::-1]:
    if col == "#":
        break
    res += 1

for col in y_col[X:]:
    if col == "#":
        break
    res += 1

print(res)
