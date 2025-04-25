N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = [(i, a) for i, a in enumerate(A_list, 1)]
res_list.sort(key=lambda x: x[1])
print(res_list[-2][0])