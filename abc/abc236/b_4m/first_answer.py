N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = [0] * N
for a in A_list:
    res_list[a-1] += 1

print(res_list.index(3)+1)