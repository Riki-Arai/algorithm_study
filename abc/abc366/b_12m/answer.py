N = int(input())
S_lists = [list(input()) for _ in range(N)] # 取得例：[A1、A2・・・An]、N行の入力用

M = max(map(len, S_lists)) 
res_list = []
for i in range(M):
    res = ""
    for j in range(N-1, -1, -1):
        if i < len(S_lists[j]):
            res += S_lists[j][i] 
        else:
            res += "*"
    res_list.append(res)

for res in res_list:
    print(res.rstrip("*"))