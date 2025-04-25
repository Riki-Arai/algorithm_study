N = int(input())
P_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_dic = {}
for i, p in enumerate(P_list, 2):
    res_dic[i] = p

res = 0
for _ in range(100):
    res += 1
    N = res_dic[N]
    if N == 1:
        print(res)
        exit()