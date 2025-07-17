# 尺取法と呼ばれるテクニック
# 一見すると計算量が二重ループ分に見えるが、実際にはO(N)らしい
from collections import deque

N = int(input().strip())
A_list = list(map(int, input().split()))

q = deque()
res = 0

for c in A_list:
    # deque の右端に要素を一つ追加
    q.append(c)
    # 条件を満たさなくなった時にpopleftで除外
    # テンプレートでも条件を満たさない時にpopleftする実装になっていたが、長さの条件は前提なのでそちらは満たす必要がある
    while len(q) >= 3 and not ((q[-1] - q[-2]) != (q[-2] - q[-3])):
        q.popleft()
    ######### 注意 #########
    # 非常に大事なのが右端は常に最新奈状態で、かつ固定したという前提で条件を満たす(l,r)の組をカウントしているという点
    # (3)で条件を満たすl,rは右端rを固定して(1,1)、(3,6)なら(2,2)と(1,2)、(3,6,9)なら(3,3)と(2,3)と(1,3)といった具合にカウントするので重複しない
    res += len(q)

print(res)