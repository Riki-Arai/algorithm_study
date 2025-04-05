import copy

N = int(input())
A_lists = [input().split() for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]
B_lists = [input().split() for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

b_set = set()
for i in range(N):
    for j in range(N):
        if B_lists[i][j] == "1":
            b_set.add((i, j))

count = 0
tmp_A_lists = copy.deepcopy(A_lists)
while True:
    for i in range(N):
        for j in range(N):
            tmp_A_lists[i][j] = A_lists[N-1-j][i]

    A_lists = copy.deepcopy(tmp_A_lists)
    a_set = set()
    for i in range(N):
        for j in range(N):
            if A_lists[i][j] == "1":
                a_set.add((i, j))

    if a_set <= b_set:
        print("Yes")
        exit()

    count += 1
    if count == 4:
        print("No")
        break