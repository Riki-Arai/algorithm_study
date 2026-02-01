import bisect
from collections import defaultdict

N, Q = map(int, input().split())

v_list = []
v_dict = defaultdict(int)
for n in range(1, N+1):
    v_list.append(n)
    v_dict[n] = 1

l_i = 0
for _ in range(Q):
    X, Y = map(int, input().split())
    b_i = bisect.bisect_right(v_list, X, l_i)
    res = 0
    for i in range(l_i+1, b_i+1):
        res += v_dict[i]

    if res == 0:
        print(0)
    else:
        print(res)
        v_dict[Y] += res
        l_i = max(b_i, l_i)