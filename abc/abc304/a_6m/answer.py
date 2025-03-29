N = int(input())
A_lists = [input().split() for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

init_idx = 10**10
min_age = 10**10
for i, a_list in enumerate(A_lists):
    min_age = min(min_age, int(a_list[1]))
    if min_age == int(a_list[1]): 
        init_idx = i

res_list = A_lists[init_idx:] + A_lists[:init_idx]
for x in res_list:
    print(x[0])