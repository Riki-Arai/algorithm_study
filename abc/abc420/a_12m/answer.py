X, Y = map(int, input().split()) # 取得例：1 2
if (X+Y)%12 == 0:
    print(12)
else:
    print((X+Y)%12)

