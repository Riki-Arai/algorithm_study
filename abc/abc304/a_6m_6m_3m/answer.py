N = int(input())
A_lists = [input().split() for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

age_list = list(map(lambda x: int(x[1]), A_lists))
min_age_idx = age_list.index(min(age_list))

for i in range(min_age_idx, N + min_age_idx):
    print(A_lists[i % N][0])