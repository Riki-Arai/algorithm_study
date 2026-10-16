'''
(1) Aに存在しないものをSotedSetに格納したいが、制約が大きいのでそれはできないと思ってしまっていた
(2) インデックスと値が一致する限りは連続している（=True)、そうでなければそれ以降はFalseという性質があることを発見
(3) そこでその区切りとなる値を二分探索で取得し、さらにSortedSset内でも二分探索をすればかろうじで間に合う
    → 二分探索で値を決めて、さらに数列を二分探索をするという考え方は応用が効きそうなので意識しておく
(4) 以上の解き方でもできはしたが、実際にはMexの最大値がN+1なのでそもそもAに存在しないものを管理することができた・・・・
(5) 補集合に着目することはできていたが、上限を正しく把握するべきだった
'''
from sortedcontainers import SortedSet
from collections import Counter

N, Q = map(int, input().split())
A_list = list(map(int, input().split()))

res = 0
sa_set = SortedSet(A_list)
a2c_dict = Counter(A_list)

def is_ok(n):
    # nの挿入位置がnなら、
    # 0～n-1がすべてsa_setに存在している
    return sa_set.bisect_left(n) == n

for _ in range(Q):
    i, x = map(int, input().split())

    if a2c_dict[A_list[i-1]] - 1 == 0:
        sa_set.discard(A_list[i-1])
    a2c_dict[A_list[i-1]] -= 1

    if a2c_dict[x] + 1 == 1:
        sa_set.add(x)
    a2c_dict[x] += 1

    A_list[i-1] = x

    ok, ng = 0, N + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2

        if is_ok(mid):
            ok = mid
        else:
            ng = mid

    print(ok)