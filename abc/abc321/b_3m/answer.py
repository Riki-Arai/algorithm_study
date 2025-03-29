N, X = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

for x in range(0, 101):
    tmp_A_list = A_list.copy()
    tmp_A_list.append(x)
    tmp_A_list.sort()
    if sum(tmp_A_list[1:-1]) >= X:
        print(x)
        exit()

print(-1)