from sortedcontainers import SortedSet
from collections import Counter

N, Q = map(int, input().split())
A_list = list(map(int, input().split()))

res = 0
sa_set = SortedSet([i for i in range(N+1)])
a2c_dict = Counter(A_list)
for k in a2c_dict.keys():
    sa_set.discard(k)

for _ in range(Q):
    i, x = map(int, input().split())

    if a2c_dict[A_list[i-1]]-1 == 0:
        sa_set.add(A_list[i-1])
    a2c_dict[A_list[i-1]] -= 1

    if a2c_dict[x]+1 == 1:
        sa_set.discard(x)
    a2c_dict[x] += 1

    A_list[i-1] = x

    print(sa_set[0])