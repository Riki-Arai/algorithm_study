N, H, X = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

for i, a in enumerate(A_list, 1):
    if H + a >= X:
        print(i)
        exit()