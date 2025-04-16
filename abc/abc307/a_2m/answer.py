N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = 0
res_list = []
for i, a in enumerate(A_list, 1):
    res += a
    if i % 7 == 0:
        res_list.append(res)
        res = 0

print(*res_list)