N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

cum = 0
for a in A_list:
    cum += a

res = 0
for i in range(N-1):
    cum -= A_list[i]
    res += cum*A_list[i]

print(res)