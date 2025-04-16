H, W = map(int, input().split())
A = [input() for _ in range(H)]
B = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        is_ok = True
        for k in range(H):
            for l in range(W):
                if A[(i+k)%H][(j+l)%W] != B[k][l]:
                    is_ok = False
        if is_ok:
            print("Yes")
            exit()

print("No")

#H, W = map(int, input().split())
#A_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]
#B_lists = [list(input()) for _ in range(H)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]
#
#a_list, b_list = [], []
#for i in range(H):
#    for j in range(W):
#        if A_lists[i][j] == "#":
#            a_list.append([i, j])
#        if B_lists[i][j] == "#":
#            b_list.append([i, j])
#
#for i in range(H+1):
#    for j in range(W+1):
#        c_a_list = list(map(lambda x: [(x[0]-i)%H, x[1]], a_list))
#        c_a_list = list(map(lambda x: [x[0], (x[1]+j)%W], c_a_list))
#        if sorted(c_a_list) == sorted(b_list):
#            print("Yes")
#            exit()
#        del c_a_list
#
#print("No")