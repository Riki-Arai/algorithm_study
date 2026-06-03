from sortedcontainers import SortedList

N, K = map(int, input().split())
P_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res_lists = []
for i, p in enumerate(P_list):
    res_lists.append([p, i])

res = float("INF")
i_list = SortedList()
res_lists.sort()
for i, res_list in enumerate(res_lists, 1):
    i_list.add(res_list[1])
    if len(i_list) == K:
        res = min(i_list[-1]-i_list[0], res)
        i_list.remove(res_lists[i-K][1])

print(res)