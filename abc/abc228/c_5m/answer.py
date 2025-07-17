N, K = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

score_list = []
for A_list in A_lists:
    score_list.append(sum(A_list))

sort_score_list = sorted(score_list, reverse=True)
base_score = sort_score_list[K-1]
for score in score_list:
    if score + 300 >= base_score:
        print("Yes")
    else:
        print("No")