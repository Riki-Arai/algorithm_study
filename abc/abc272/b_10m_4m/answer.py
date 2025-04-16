N, M = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(M)] # 取得例:[[1,2], [3,4]・・[9,10]]

res_list = []
for _ in range(20):
    for i in range(11, -1, -1):
        if 3 ** i <= M:
            M -= 3 ** i
            res_list.append(i)
            if M == 0:
                break

print(*res_list)