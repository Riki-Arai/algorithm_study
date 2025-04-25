N = int(input()) # 数値
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = float("INF")
for i, A_list in enumerate(A_lists):
    for j, B_list in enumerate(A_lists):
        x, y = A_list
        xx, yy = B_list
        if i == j:
            res = min(x+y, res)
        else:
            res = min(min(max(y, xx), max(x, yy)), res)

print(res)

## first
#N = int(input()) # 数値
#A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]
#
#res_list = []
#for i, x in enumerate(A_lists, 1):
#    a = x[0]
#    for j, y in enumerate(A_lists, 1):
#        b = y[1]
#        if i == j:
#            res_list.append(a + b)
#        else:
#            res_list.append(max(a, b))
#
#print(min(res_list))
#