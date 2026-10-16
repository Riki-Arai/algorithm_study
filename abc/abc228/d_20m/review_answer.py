#  SortedDictはlistやsetの値を持てる、peekitem(bisect_left(1))のイメージで1に近いキーの値を取得可能
from sortedcontainers import SortedSet

Q = int(input())
N = 2**20

s_set = SortedSet([i for i in range(N)])
res_list = [-1]*N
for _ in range(Q):
    t, x = map(int, input().split())
    x_i = x%N
    if t == 1:
        if x_i in s_set:
            s_set.discard(x_i)
            res_list[x_i] = x
        else:
            b_i = s_set.bisect_left(x_i)
            if b_i == len(s_set):
                x_ii = s_set[0]
                res_list[x_ii] = x
                s_set.discard(x_ii)
            else:
                x_ii = s_set[b_i]
                res_list[x_ii] = x
                s_set.discard(x_ii)
    else:
        print(res_list[x_i])



from sortedcontainers import SortedSet

Q = int(input())

N = 2 ** 20
A = [-1] * N
ss = SortedSet(range(N)) # Aの要素が-1であるもののインデックスの集合
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        # Aの第x項以降にある最初の-1を、x書き換える
        idx = ss.bisect_left(x % N) # x>=N の可能性があるので x%N にする
        if idx == len(ss):
            idx = 0
        A[ss[idx]] = x
        ss.discard(ss[idx])
    elif t == 2:
        print(A[x % N])