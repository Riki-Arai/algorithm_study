N, M = map(int, input().split())
S_list = [input() for _ in range(N)] # 取得例：[A1、A2・・・An]、N行の入力用
T_list = [input() for _ in range(M)] # 取得例：[A1、A2・・・An]、N行の入力用

res = 0
for s in S_list:
    if s[-3:] in T_list:
        res += 1
print(res)