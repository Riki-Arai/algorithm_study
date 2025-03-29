N, M = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]

for i in range(N):
    for j in range(N):
        if A_lists[i][0] >= A_lists[j][0] and set(A_lists[j][2:]) >= set(A_lists[i][2:]):
            if A_lists[i][0] > A_lists[j][0] or len(set(A_lists[j][1:])-set(A_lists[i][1:])) > 0:
                print("Yes")
                exit()

print("No")