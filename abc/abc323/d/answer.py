from collections import defaultdict, Counter, deque

N = int(input())

X_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]
X_lists.sort()
n_dict = defaultdict(int)
for s, c in X_lists:
    n_dict[s] = c

res = 0
while len(n_dict):
    k = list(n_dict.keys())[0]
    if n_dict[k] >= 2:
        if n_dict[k]%2 == 1:
            res += 1
        n_dict[2*k] += n_dict[k]//2
        del n_dict[k]
    else:
        res += 1
        del n_dict[k]

print(res)