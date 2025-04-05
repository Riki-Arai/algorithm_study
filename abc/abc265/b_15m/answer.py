N, M, T = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
X_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]

dic_ = {}
for x in X_lists:
    dic_[x[0]-1] = x[1]

res = 0
for i in range(N-1):
    if i in dic_:
        T += dic_[i]
    res += A_list[i]
    if res >= T:
        print("No")
        exit()

print("Yes")