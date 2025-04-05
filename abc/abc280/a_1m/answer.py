H, W = map(int, input().split())
A_list = [input() for _ in range(H)] # 取得例：[A1、A2・・・An]、N行の入力用

res = 0
for a in A_list:
    res += a.count("#")

print(res)