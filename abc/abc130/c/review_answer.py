W, H, x, y = map(int, input().split()) # 取得例：1 2

if 2*x == W and 2*y == H:
    print(W*H/2, 1)
else:
    print(W*H/2, 0)