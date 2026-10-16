'''
(1) DPの線を考えたが、管理すべき状態が多いかもしれないので断念
(2) 連続区間の問題であり、単調性もあるかもしれないことから尺取法に着目
(3) 余事象も考えたが、結局はそのままの方が良さそう
(4) 条件の確認に悩んだが、SortedListを活用することで解決
(5) 区間
'''
from sortedcontainers import SortedList
from collections import deque

N, D = map(int, input().split())
A_list = list(map(int, input().split()))

res = 0
max_v, min_v = 10**9, 1
dq = deque()
s_list = SortedList()
D -= 1
for a in A_list:
    s_list.add(a)
    dq.append(a)
    
    r = min(a + D, max_v)
    l = max(a - D, min_v)
    
    count = s_list.bisect_right(r) - s_list.bisect_left(l)
    while len(dq) > 0 and count > 1:
        p_a = dq.popleft()
        if l <= p_a <= r:
            count -= 1
            
        s_list.remove(p_a)
            
    res += len(dq)

print(res)