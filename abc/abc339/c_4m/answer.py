N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = 0
for a in A_list:
    res = max(res+a, 0)

print(res)