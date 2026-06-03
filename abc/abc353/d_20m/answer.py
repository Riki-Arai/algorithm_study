N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = 0
sum_ = sum(A_list)
s_a_list = list(reversed(A_list))
for i in range(N-1):
    a = s_a_list[i]
    sum_ -= a
    res = (sum_*(10**len(str(a))) + (N-(i+1))*a + res) % 998244353

print(res)