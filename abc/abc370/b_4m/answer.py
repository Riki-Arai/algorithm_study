N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
for i in range(N):
    if i >= res:
        res = A_lists[i][res] - 1
    else:
        res = A_lists[res][i] - 1

print(res+1)