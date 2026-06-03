N = int(input()) # 数値：1
d_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
for i in range(N):
    for j in range(i+1, N):
        res += d_list[i]*d_list[j]

print(res)