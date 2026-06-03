import math

N, D = map(int, input().split()) # 取得例：1 2
X_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

res = 0
for i in range(N):
    for j in range(i+1, N):
        tmp_res = 0
        for k in range(D):
            tmp_res += pow(X_lists[i][k]-X_lists[j][k], 2)
        tmp_res = math.sqrt(tmp_res)
        if float(int(tmp_res)) == float(tmp_res):
            res += 1

print(res)