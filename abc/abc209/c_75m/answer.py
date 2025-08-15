N = int(input())
C_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = 0
for i in range(1, N):
    f_n = C_list[i-1]
    s_n = C_list[i]
    if f_n > s_n:
        res = (res + (s_n-i+1) * (s_n-i)) % (10**9+7)
        res = (res + (f_n-s_n) * s_n) % (10**9+7)
    else:
        res += (res + (f_n-i+1) * (s_n-i)) % (10**9+7)

print(res)