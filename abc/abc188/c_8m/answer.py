N = int(input()) # 取得例：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res_lists = []
for i, a in enumerate(A_list, 1):
    res_lists.append((i, a))

for _ in range(N+1):
    new_res_lists = []
    for j in range(0, len(res_lists)-1, 2):
        i, a = res_lists[j]
        ii, aa = res_lists[j+1]
        if a > aa:
            if len(res_lists) == 2:
                print(ii)
                exit()
            new_res_lists.append((i, a))
        else:
            if len(res_lists) == 2:
                print(i)
                exit()
            new_res_lists.append((ii, aa))

    res_lists = new_res_lists