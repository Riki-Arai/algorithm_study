N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = 0
for a in A_list:
    if a >= 10:
        res += a - 10

print(res)