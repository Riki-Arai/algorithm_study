N, Q = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

cum_ = 0
for i in range(N):
    cum_ += min(A_list[i], B_list[i])

for _ in range(Q):
    c, X, V = input().split()
    X, V = int(X), int(V)
    if c == "A":
        cum_ = cum_ + (min(V, B_list[X-1]) - min(A_list[X-1], B_list[X-1]))
        A_list[X-1] = V
        print(cum_)
    else:
        cum_ = cum_ + (min(V, A_list[X-1]) - min(A_list[X-1], B_list[X-1]))
        B_list[X-1] = V
        print(cum_)
