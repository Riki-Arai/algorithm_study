from collections import defaultdict

N, W = map(int, input().split()) # 取得例：1 2
input_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

input_lists.sort(key=lambda x: (x[0], x[1]))
t2p_dict = defaultdict(int)
for s, t, p in input_lists:
    t2p_dict[s] += p
    t2p_dict[t] -= p

t2p_lists = list(t2p_dict.items())
t2p_lists.sort()
need_w = 0
for t, p in t2p_lists:
    need_w += p
    if need_w > W:
        print("No")
        exit()

print("Yes")