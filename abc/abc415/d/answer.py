N, M = map(int, input().split()) # 取得例：1 2
X_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]

x_lists = []
for a, b in X_lists:
    x_lists.append((a, a-b))

res = 0
x_lists.sort(key=lambda x: x[1])
for a, d in x_lists:
    if N >= a:
        m = (N-a)//d
        res += (m+1)
        N -= (d*m+d)

print(res)