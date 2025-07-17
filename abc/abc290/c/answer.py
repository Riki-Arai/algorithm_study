N, K = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

A_list.sort()
for i, a in enumerate(A_list):
    if i == K-1:
        print(K)
        exit()
    elif i != a:
        print(A_list[i]+1)
        exit()