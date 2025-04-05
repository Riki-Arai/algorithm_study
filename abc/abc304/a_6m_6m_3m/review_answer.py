N = int(input())
A_lists = [input().split() for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

age_list = list(map(lambda x: int(x[1]), A_lists))
min_age_idx = age_list.index(min(age_list))

for i in range(min_age_idx, N + min_age_idx):
    print(A_lists[i % N][0])

### second
#N = int(input())
#A_lists = [input().split() for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]
#
#min_v = float("INF")
#for i, A_list in enumerate(A_lists):
#    S, A = A_list[0], int(A_list[1])
#    min_v = min(min_v, A)
#    if A == min_v:
#        min_age_idx = i
#
#for i in range(min_age_idx, N + min_age_idx):
#    print(A_lists[i%N][0])


### first
#N = int(input())
#A_lists = [input().split() for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]
#
#init_idx = 10**10
#min_age = 10**10
#for i, a_list in enumerate(A_lists):
#    min_age = min(min_age, int(a_list[1]))
#    if min_age == int(a_list[1]):
#        init_idx = i
#
#res_list = A_lists[init_idx:] + A_lists[:init_idx]
#for x in res_list:
#    print(x[0])