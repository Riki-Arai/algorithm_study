N, M = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(N)]

n = A_lists[0][0]
# 0-baseに変換しようとするとx−1=(i−1)×7+(j−1)になるので、以下の式で0-baseのiとjを決定できる
i, j = divmod(n-1, 7)
for k in range(N):
    ii = i + k
    for l in range(M):
        jj = j + l
        m, r = divmod(A_lists[k][l]-1, 7)
        if m != ii:
            print("No")
            exit()
        elif r != jj:
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