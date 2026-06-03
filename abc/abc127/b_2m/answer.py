r, D, X = map(int, input().split()) # 取得例：1 2

for x in range(10):
    X = r*X - D
    print(X)