N = int(input())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

t_score, a_score = 0, 0
for A_list in A_lists:
    t_score += A_list[0]
    a_score += A_list[1]

if t_score > a_score:
    print("Takahashi")
elif t_score == a_score:
    print("Draw")
else:
    print("Aoki")