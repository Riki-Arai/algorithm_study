N, T = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

sum_ = sum(A_list)
T = T % sum_

for i in range(N):
    if T <= A_list[i]:
        print(i+1, T)
        exit()
    T -= A_list[i]