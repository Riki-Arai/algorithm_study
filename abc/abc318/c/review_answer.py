N, D, P = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

A_list.sort(reverse=True)
res = 0
for i in range(0, N, D):
    # チケットの期間内の総額とPを比較して安い方を採用していく
    res+= min(sum(A_list[i:i+D]), P)

print(res)