N, P, Q = map(int, input().split())
D_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

if P > min(D_list) + Q:
    print(min(D_list) + Q)
else:
    print(P)