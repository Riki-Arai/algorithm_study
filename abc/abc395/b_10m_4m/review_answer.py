N = int(input())

grid_lists = [["?"]*N for _ in range(N)]
for i in range(N):
    for j in range(N+1-i):
        if j >= i:
            if i%2 == 0:
                for ii in range(i, j):
                    for jj in range(i, j):
                        grid_lists[ii][jj] = "#"
            else:
                for ii in range(i, j):
                    for jj in range(i, j):
                        grid_lists[ii][jj] = "."


for grid_list in grid_lists:
    print("".join(grid_list))

#N = int(input())
#A_lists = [["*"]*N for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]
#
## iとjをインデックスに使用しているので0ベースにして考える
#for i in range(N):
#    for j in range(N-i):
#        if i <= j and i % 2 == 0:
#            for ii in range(i, j+1): #j*1をしてあげる
#                for jj in range(i, j+1):
#                    A_lists[ii][jj] = "#"
#        elif i <= j and i % 2 == 1:
#            for ii in range(i, j+1):
#                for jj in range(i, j+1):
#                    A_lists[ii][jj] = "."
#
#for A_list in A_lists:
#    print("".join(A_list))

#N = int(input())
#A_lists = [["*"]*N for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]
#
#for i in range(N):
#    j = N - i
#    if i > j:
#        continue
#    else:
#        if i % 2 == 0:
#            for k in range(i, j):
#                for l in range(i, j):
#                    A_lists[k][l] = "#"
#        else:
#            for k in range(i, j):
#                for l in range(i, j):
#                    A_lists[k][l] = "."
#
#for A_list in A_lists:
#    print("".join(A_list))