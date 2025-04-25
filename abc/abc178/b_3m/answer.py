a, b, c ,d = map(int, input().split()) # 取得例：1 2

res = -10**10 * 10**10
x_list = [a, b]
y_list = [c, d]
for x in x_list:
    for y in y_list:
        res = max(res, x*y)

print(res)