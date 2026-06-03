from sortedcontainers import SortedDict

N = int(input())

X_lists = [list(map(int, input().split())) for _ in range(N)]
X_lists.sort()

n_dict = SortedDict()
for s, c in X_lists:
    n_dict[s] = n_dict.get(s, 0) + c

res = 0
while n_dict:
    k = n_dict.keys()[0]
    count = n_dict[k]
    if count >= 2:
        if count % 2 == 1:
            res += 1
        n_dict[2 * k] = n_dict.get(2 * k, 0) + (count // 2)
    else:
        res += 1

    del n_dict[k]

print(res)



from sortedcontainers import SortedDict


N = int(input())

s2n_dict = SortedDict(int)
for _ in range(N):
    S, C = map(int, input().split())
    s2n_dict[S] = C

res = 0
while len(s2n_dict):
    k = s2n_dict.keys()[0]
    v = s2n_dict[k]
    if v >= 2:
        if v%2 == 0:
            v //= 2
            if 2*k in s2n_dict:
                s2n_dict[2*k] += v
            else:
                s2n_dict[2*k] = v
        else:
            v //= 2
            if 2*k in s2n_dict:
                s2n_dict[2*k] += v
            else:
                s2n_dict[2*k] = v
            res += 1
    else:
        res += 1

    del s2n_dict[k]

print(res)