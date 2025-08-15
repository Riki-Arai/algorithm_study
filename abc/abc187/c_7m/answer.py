N = int(input()) # 取得例：1
S_list = [input() for _ in range(N)] # 取得例：[A1,A2・・・An]、N行の入力用

res_set = set()
for s in S_list:
    res_set.add(s)

for s in S_list:
    if "!" + s in res_set:
        print(s)
        exit()

print("satisfiable")