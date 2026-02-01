N = int(input()) # 数値：1
S_list = [input() for _ in range(N)] # 取得例：["A","B"・・・"E"]、N行の入力用

res_set = set()
for i in range(N):
    for j in range(N):
        if i != j:
            res_set.add(S_list[i]+S_list[j])

print(len(res_set))