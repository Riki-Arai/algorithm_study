A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = 0
for i in range(1, 5):
    res += A_list.count(i) // 2
print(res)