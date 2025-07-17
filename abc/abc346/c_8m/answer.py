N, K = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

sum_ = 0
n_set = set()
for a in A_list:
    if a not in n_set and 1 <= a <= K:
        n_set.add(a)
        sum_ += a

n_sum = ((1+K)*K) // 2
print(n_sum-sum_)