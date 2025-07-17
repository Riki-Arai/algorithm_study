n, a, b = map(int, input().split())

s = [["." for _ in range(n*b)] for _ in range(n*a)]

for i in range(n*a):
    for j in range(n*b):
        # aやbごとに数が1ずつ大きくなるように調整
        r = i // a
        c = j // b
        # 市松模様系の問題は縦と横のインデックスの和の偶奇で決める
        if (r + c) % 2 == 1:
            s[i][j] = '#'

for row in s:
    print("".join(row))


## first
#N, A, B = map(int, input().split())
#res_lists = [["*"]*B*N for _ in range(A*N)]
#
#v_count = 0
#for i in range(0, N*A, A):
#    w_count = 0
#    for j in range(0, N*B, B):
#        if v_count % 2 == 0:
#            if w_count % 2 == 0:
#                for a in range(A):
#                    for b in range(B):
#                        res_lists[i+a][j+b] = "."
#            else:
#                for a in range(A):
#                    for b in range(B):
#                        res_lists[i+a][j+b] = "#"
#        else:
#            if w_count % 2 == 0:
#                for a in range(A):
#                    for b in range(B):
#                        res_lists[i+a][j+b] = "#"
#            else:
#                for a in range(A):
#                    for b in range(B):
#                        res_lists[i+a][j+b] = "."
#
#        w_count += 1
#
#    v_count += 1
#
#
#for res_list in res_lists:
#    print("".join(res_list))