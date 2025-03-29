A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = 0
for i, a in enumerate(A_list):
    res += 2**i*a
print(res)