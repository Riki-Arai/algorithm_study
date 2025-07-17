X, Y = map(int, input().split()) # 取得例：1 2

for i in range(X+1):
    for j in range(X+1):
        if i + j == X and i*2 + j*4 == Y:
            print("Yes")
            exit()

print("No")