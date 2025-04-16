N, K = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = [i for i, a in enumerate(A_list, 1) if a == max(A_list)]
for res in res_list:
    if res in B_list: # a_set & b_setとした方がスマートではあった
        print("Yes")
        exit()
print("No")