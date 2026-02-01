from collections import defaultdict

N, T = map(int, input().split())

n2s_dict = defaultdict(int)
s2n_dict = defaultdict(int)
for i in range(1, N+1):
    n2s_dict[i] = 0
    s2n_dict[0] += 1

res_set = set([0])
for _ in range(T):
    A, B = map(int, input().split())
    s = n2s_dict[A]
    if s in s2n_dict and s2n_dict[s] == 1:
        s2n_dict[s] = 0
        res_set.discard(s)
    else:
        s2n_dict[s] -= 1

    s2n_dict[s+B] += 1
    n2s_dict[A] = s + B
    res_set.add(s+B)
    print(len(res_set))