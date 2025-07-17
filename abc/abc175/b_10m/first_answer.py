N = int(input()) # 取得例：1
L_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res_set = set()
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            ii, jj, kk = L_list[i], L_list[j], L_list[k]
            if ii != jj and jj != kk and kk != ii:
                if ii + jj > kk and jj + kk > ii and kk + ii > jj:
                    res_set.add((i+1, j+1, k+1))

print(len(res_set))