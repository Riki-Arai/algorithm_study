import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1

res_lists = [[] for _ in range(N+1)]
for i in range(1, N+1):
    input_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
    for b in input_list[1:]:
        res_lists[b].append(i)

for res_list in res_lists[1:]:
    print(len(res_list), *res_list)