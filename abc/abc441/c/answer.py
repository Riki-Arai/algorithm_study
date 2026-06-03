N, K, X = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

A_list.sort(reverse=True)
sum_ = 0
res = N-K
for a in A_list[N-K:]:
    res += 1
    sum_ += a
    if sum_ >= X:
        print(res)
        exit()

print(-1)