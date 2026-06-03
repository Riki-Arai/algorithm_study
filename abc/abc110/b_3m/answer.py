import bisect as bi

N, M, X, Y = map(int, input().split()) # 取得例：1 2

x_list = sorted(list(map(int, input().split())))
y_list = sorted(list(map(int, input().split())))
for z in range(X+1, Y):
    x_i = bi.bisect_left(x_list, z)
    y_i = bi.bisect_left(y_list, z)
    if x_i == len(x_list) and y_i == 0:
        print("No War")
        exit()

print("War")