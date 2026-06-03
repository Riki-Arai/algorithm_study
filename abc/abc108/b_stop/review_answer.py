x1, y1, x2, y2 = map(int, input().split()) # 取得例：1 2 res_lists = []

res_list = []
for _ in range(2):
    vec_x = -(y2-y1)
    vec_y = x2-x1

    x1 = x2
    y1 = y2
    x2 += vec_x
    y2 += vec_y
    res_list.append(str(x2))
    res_list.append(str(y2))

print(*res_list)