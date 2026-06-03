N, X = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

for a in A_list:
    if a < X:
        X = a
        print(1)
    else:
        print(0)