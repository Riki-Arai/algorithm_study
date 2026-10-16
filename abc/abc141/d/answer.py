'''
(1) 値段が一番高いものから順番に割引を適用（貪欲法）
(2) 優先度付きキューやソートリストを使うことで常に値段が高いものを取得できるのでそちらを利用して解く
'''

import heapq as hq

N, M = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

a_list = [-a for a in A_list]
hq.heapify(a_list)
while M > 0:
    a = -1*hq.heappop(a_list)
    a //= 2
    hq.heappush(a_list, -1*a)
    M -= 1

print(-1*sum(a_list))