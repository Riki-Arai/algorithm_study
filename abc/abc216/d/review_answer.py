'''
解説AC
(1) キューを使うと良さそうだが、同じ筒からボールを取り出さない仕組みをどうするか（これが最初はできなかった）
(2) 一番上のボールを取り出せる筒のインデックスをキューで管理し、これが0になるまで行うような仕組みにする
(3) 1個目のボールを取り出した時は取り出した時の筒のインデックスとボールの番号を管理
(4) 2個目のボールを取り出した時は(3)と取り出したインデックスをまたキューに戻す（(3)の情報は削除しておくがどちらでもいいかも）
'''
from collections import deque

N, M = map(int, input().split())

a_lists = []
for _ in range(M):
    k = int(input().strip())
    a_list = list(map(int, input().split()))
    a_lists.append(a_list[::-1])

b_set = set()
b2i_list = [None]*(N+1)
dq = deque([i for i in range(M)])
while len(dq):
    i = dq.popleft()
    if not len(a_lists[i]):
        continue
    b = a_lists[i].pop()
    if b not in b_set:
        b_set.add(b)
        b2i_list[b] = i
    else:
        dq.append(i)
        ii = b2i_list[b]
        dq.append(ii)
        b_set.discard(b)
        b2i_list[b] = None

if sum(map(len, a_lists)) == 0:
    print("Yes")
else:
    print("No")