N, M = map(int, input().split()) # 取得例：1 2

drink_set = set()
for _ in range(N):
    L = int(input()) # 数値：1
    X_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
    for x in X_list:
        if x not in drink_set:
            print(x)
            drink_set.add(x)
            break
    else:
        print(0)