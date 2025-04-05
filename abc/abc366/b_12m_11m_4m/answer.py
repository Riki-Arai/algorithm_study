N = int(input())
S_lists = [list(input()) for _ in range(N)] # 取得例：[A1、A2・・・An]、N行の入力用

M = max(map(len, S_lists))
for i in range(M):
    res = ""
    for j in range(N):
        if i < len(S_lists[j]):
            res += S_lists[j][i]
        else:
            res += "*"
    print(res[::-1].rstrip("*"))
