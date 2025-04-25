N, X = map(int, input().split()) # 取得例：1 2
S_list = list(input()) # 取得例：["A","B"・・・]

for s in S_list:
    if s == "x":
        X = max(0, X - 1)
    else:
        X += 1

print(X)