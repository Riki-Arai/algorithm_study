N, K, Q = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
Q_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = [i in A_list for i in range(1, N+1)]
for q in Q_list:
    if res_list[A_list[q-1]-1] == True and A_list[q-1] < len(res_list) and res_list[A_list[q-1]] == False:
        res_list[A_list[q-1]-1] = False
        res_list[A_list[q-1]] = True
        A_list[q-1] += 1

print(*A_list)