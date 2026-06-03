N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

MOD = 998244353
dp_lists = [[0]*10 for _ in range(N)]
a, b = A_list[0], A_list[1]
dp_lists[1][(a+b)%10] += 1
dp_lists[1][a*b%10] += 1
for i in range(2, N):
    a = A_list[i]
    for j in range(9, -1, -1):
        if dp_lists[i-1][j]:
            dp_lists[i][(j+a)%10] = (dp_lists[i][(j+a)%10] + dp_lists[i-1][j]) % MOD
            dp_lists[i][(j*a)%10] = (dp_lists[i][(j*a)%10] + dp_lists[i-1][j]) % MOD

for i in range(10):
    print(dp_lists[N-1][i])