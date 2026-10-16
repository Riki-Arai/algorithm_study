import heapq as hq
from sortedcontainers import SortedSet

N, K = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

A_list.sort()
dq_list = A_list.copy()
hq.heapify(dq_list)
res_set = SortedSet()
seen_set = set()
while len(res_set) < K:
    n = hq.heappop(dq_list)
    res_set.add(n)
    for a in A_list:
        if n+a not in seen_set:
            seen_set.add(n+a) # res_setにaddするとres_set内の要素とaを足した時により小さいものがある可能性があるのに、その前にK個以上の要素になってしまうのでseen_setを利用
            hq.heappush(dq_list, n+a)

print(res_set[K-1])