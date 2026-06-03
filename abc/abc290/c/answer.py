N, K = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

a_set = set(A_list)
for k in range(K+1):
    if k not in a_set:
        print(k)
        exit()

print(k)