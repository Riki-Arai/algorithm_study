N = int(input()) # 取得例：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

cum = 0
for i in range(N):
    cum += A_list[i]

res = 0
for a in A_list:
    res += a*(cum-a)
    cum -= a

print(res % (10**9+7))