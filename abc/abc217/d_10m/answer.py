import bisect
from sortedcontainers import SortedList

L, Q = map(int, input().split())
res_list = SortedList()
res_list.add(0)
res_list.add(L)
for _ in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        res_list.add(x)
    else:
        if len(res_list) == 2:
            print(L)
        else:
            b_i = bisect.bisect_left(res_list, x)
            print(res_list[b_i]-res_list[b_i-1])