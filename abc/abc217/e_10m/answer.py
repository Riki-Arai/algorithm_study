'''
(1) 2の左端の出力&削除、3のソートを素直にやってしまうとTLE
(2) ソート済みの情報はほしいが毎回ソートは難しい。そこで必要分だけソートするようにaddをする形を考える
(3) 必要分だけ追加する処理はせいぜいQ個ほどなので、計算量も間に合いそう
'''
from sortedcontainers import SortedList
from collections import deque

Q = int(input()) # 数値：1

dq = deque()
s_list = SortedList()
for _ in range(Q):
    input_ = input().strip()
    if input_[0] == '1':
        dq.append(int(input_.split()[1]))
    elif input_[0] == '2':
        if len(s_list):
            print(s_list[0])
            s_list.discard(s_list[0])
        else:
            print(dq.popleft())
    else:
        while len(dq):
            s_list.add(dq.popleft())