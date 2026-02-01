N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
for i, a in enumerate(A_list, 1):
    if i % 2 != 0:
        res += a

print(res)