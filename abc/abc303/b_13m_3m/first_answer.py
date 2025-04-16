import itertools

N, M = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]

res_set = set()
for A_list in A_lists:
    for i in range(1, N):
        #tmp_list = [A_list[i-1], A_list[i]]
        #tmp_list.sort()
        #res_set.add((tmp_list[0], tmp_list[1]))
        p, q = sorted((A_list[i - 1], A_list[i]))
        res_set.add((p, q))

all_set = set(list(itertools.combinations([i for i in range(1, N+1)], 2)))
print(len(all_set-res_set))