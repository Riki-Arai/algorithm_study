N, K, X = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

A_list.sort(reverse=True)
for i in range(len(A_list)):
    n = A_list[i]//X
    if K-n <= 0:
        A_list[i] -= K*X
        print(sum(A_list))
        exit()
    K -= n
    A_list[i] %= X

A_list.sort(reverse=True)
for j in range(K):
    if len(A_list) == j:
        break
    A_list[j] = 0

print(sum(A_list))