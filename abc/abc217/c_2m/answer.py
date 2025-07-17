N = int(input())
Q_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_list = [None]*(N+1)
for i, q in enumerate(Q_list, 1):
    res_list[q] = i

print(*res_list[1:])