N, D = map(int, input().split())
T_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

for i in range(1, len(T_list)):
    if T_list[i] - T_list[i-1] <= D:
        print(T_list[i])
        exit()

print(-1)