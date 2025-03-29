M = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

mdl = int((sum(A_list)+1) / 2)
for i, a in enumerate(A_list, 1):
    if mdl - a <= 0:
        print(i, mdl)
        exit()
    mdl -= a