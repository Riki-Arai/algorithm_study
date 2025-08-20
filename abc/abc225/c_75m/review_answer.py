N, M = map(int, input().split())
A_lists = [list(map(int, input().split())) for _ in range(N)]

n = A_lists[0][0]
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

#N, M = map(int, input().split())
#A_lists = [list(map(int, input().split())) for _ in range(N)]
#
#base_idx = ((A_lists[0][0]-1)//7, (A_lists[0][0]-1)%7)
#for i in range(N):
#    i_idx = base_idx[0] + i
#    for j in range(M):
#        j_idx = base_idx[1] + j
#        if i_idx*7 + j_idx != A_lists[i][j]-1:
#            print("No")
#            exit()
#
#        if not(i_idx*7 <= i_idx*7 + j_idx <= i_idx*7+6):
#            print("No")
#            exit()
#
#print("Yes")