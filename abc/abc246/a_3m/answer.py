xy_lists = [list(map(int, input().split())) for _ in range(3)] # 取得例:[[1,2], [3,4]・・[9,10]]

x_list = list(map(lambda x: x[0],xy_lists))
y_list = list(map(lambda x: x[1],xy_lists))

for x in x_list:
    if x_list.count(x) == 1:
        res_x = x
        break

for y in y_list:
    if y_list.count(y) == 1:
        res_y = y
        break

print(res_x, res_y)