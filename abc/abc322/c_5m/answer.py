N, M = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

a_idx = 0
for i in range(1, N+1):
    if A_list[a_idx] - i == 0:
        a_idx += 1
        print(0)
    else:
        print(A_list[a_idx] - i)
