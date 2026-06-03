N, M = map(int, input().split())
B_lists = [list(map(int, input().split())) for _ in range(N)]

b = B_lists[0][0]
base_i = (b-1)//7
base_j = (b-1)%7
# Mは切り出した横幅であることがポイントになる
# B_lists[0][0]が7だった場合でもM=1であれば下記の式は通過できる一方で、M=2であれば切り出し方がおかしいのでNoに該当する
if base_j + M - 1 >= 7:
    print("No")
    exit()

for i in range(N):
    for j in range(M):
        b = B_lists[i][j]
        if (base_i+i)*7+(base_j+j+1) != b:
            print("No")
            exit()

print("Yes")

## 以下のケースはWA
## 行が増えた時に同じ列において+7、列が+1ずつ増えていく条件を満たせばYesにしてしまい、改行に関して検知を行えていない
## なので改行しているかどうかも正しく検知したいケースはインデックスを活用して比較するべき
#N, M = map(int, input().split())
#A_lists = [list(map(int, input().split())) for _ in range(N)]
#
#base_i, base_j = divmod(A_lists[0][0]-1, 7)
#for i in range(N):
#    for j in range(M):
#        ii = i + base_i
#        jj = j + base_j
#        # 7 8 9 10といった改行しないパターンに対してNoだと判定できない
#        if 7*ii + jj + 1 != A_lists[i][j]:
#            print("No")
#            exit()
#
#print("Yes")