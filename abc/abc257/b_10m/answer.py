N, K, Q = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
Q_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

n_list = [False] * (N+1)
for a in A_list:
    n_list[a] = True

for q in Q_list:
    count = 0
    for i, n in enumerate(n_list):
        if n_list[i] == True:
            count += 1
        if count == q and i+1 <= N and n_list[i] and not n_list[i+1]:
            n_list[i] = False
            n_list[i+1] = True
            break

res_list = [i for i, val in enumerate(n_list) if val]
print(*res_list)