N = int(input())
S = [input() for _ in range(N)]
M = max(map(len, S))
T = [["*"] * N for _ in range(M)]
for i in range(N):
    for j in range(len(S[i])):
        T[j][N - i - 1] = S[i][j]
for i in range(M):
    while T[i][-1] == "*":
        T[i].pop()
    print("".join(T[i]))

### 以下はfirst
#N = int(input())
#S_lists = [list(input()) for _ in range(N)] # 取得例：[A1、A2・・・An]、N行の入力用
#
#max_length = max([len(S_list) for S_list in S_lists])
#S_lists.reverse()
#for i in range(max_length):
#    res = ""
#    for j in range(N):
#        if i < len(S_lists[j]):
#            res += S_lists[j][i]
#        else:
#            res += "*"
#
#    print(res.rstrip("*"))
#
#