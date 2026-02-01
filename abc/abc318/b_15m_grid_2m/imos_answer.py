N = int(input())
imos_list = [[0]*102 for _ in range(102)]

for _ in range(N):
    A, B, C, D = map(int, input().split())
    # y(行)方向をC～D, x(列)方向をA～Bとみなして2次元いもす
    imos_list[C][A] += 1
    imos_list[D][A] -= 1
    imos_list[C][B] -= 1
    imos_list[D][B] += 1

# 横方向の累積和
for i in range(102):
    for j in range(1, 102):
        imos_list[i][j] += imos_list[i][j-1]

# 縦方向の累積和
for j in range(102):
    for i in range(1, 102):
        imos_list[i][j] += imos_list[i-1][j]

res = 0
# ★ 修正ポイント：0～100 のみ集計
for i in range(101):
    for j in range(101):
        if imos_list[i][j] > 0:
            res += 1

print(res)