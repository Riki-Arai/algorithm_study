'''
(1) クエリのたびに探索をしてしまうとTLEになるので、あらかじめ頂点ごとにソート済みのリストを持つとよさそう
(2) 部分木ごとのリストを持つためには、子から親に向かって情報を持たせていく(親→子だと適切な情報を持たせることができないパターンがある)
(3) このような方法でいけるかどうかだが、K=20と小さい上に頂点も10**5程度なのでMaxでも2*10**6ほどの計算量に収まるので間に合うと思われる
(4) 余談だがs_lists[b][:20].copy()だと通常のリストになってしまうので注意(これで1時間以上詰まった)
'''
#  SortedDictはlistやsetの値を持てる、peekitem(bisect_left(1))のイメージで1に近いキーの値を取得可能
from sortedcontainers import SortedList
from collections import deque

N, Q = map(int, input().split()) # 取得例：1 2
X_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

tmp_g_lists = [set() for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split()) # 取得例：1 2
    tmp_g_lists[A].add(B)
    tmp_g_lists[B].add(A)

g_lists = [[] for _ in range(N+1)]
e_list = [0]*(N+1)
dq = deque([1])
seen_set = set([1])
while len(dq):
    a = dq.popleft()
    for b in tmp_g_lists[a]:
        if b not in seen_set:
            e_list[a] += 1
            g_lists[b].append(a)
            seen_set.add(b)
            dq.append(b)

dq = deque()
s_lists = [SortedList() for _ in range(N+1)]
seen_set = set()
for i in range(1, N+1):
    if e_list[i] == 0:
        dq.append(i)
        seen_set.add(i)
        s_lists[i].add(-1*X_list[i-1])

while len(dq):
    a = dq.popleft()

    for b in g_lists[a]:
        if b not in seen_set:
            s_lists[b].add(-1*X_list[b-1])
            seen_set.add(b)

        s_lists[b].update(s_lists[a])
        if len(s_lists[b]) > 20:
            s_lists[b] = SortedList(s_lists[b][:20].copy())

        if e_list[b]-1 == 0:
            dq.append(b)

        e_list[b] -= 1

res_list = []
for _ in range(Q):
    V, K = map(int, input().split()) # 取得例：1 2
    res_list.append(-1*s_lists[V][K-1])

for res in res_list:
    print(res)