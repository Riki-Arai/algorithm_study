N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
K = int(input()) # 数値：1

res = 0
for a in A_list:
    if K <= a:
        res += 1
print(res)