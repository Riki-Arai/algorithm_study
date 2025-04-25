N, M = map(int, input().split())
A_lists = [map(int, input().split()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

trans_A_lists = [list(row) for row in zip(*A_lists)]
for a_list in trans_A_lists:
    print(*a_list)