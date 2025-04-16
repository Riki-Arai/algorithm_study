N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = [i for i in range(N+1)]
for res in res_list:
    if A_list.count(res) == 0:
        print(res)
        exit()