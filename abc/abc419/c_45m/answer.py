N = int(input()) # 数値：1
X_lists = [list(map(int, input().split())) for _ in range(N)]





#N = int(input()) # 数値：1
#X_lists = [list(map(int, input().split())) for _ in range(N)]
#
#min_r, max_r = float("INF"), 0
#min_c, max_c = float("INF"), 0
#for r, c in X_lists:
#    min_r = min(r, min_r)
#    max_r = max(r, max_r)
#    min_c = min(c, min_c)
#    max_c = max(c, max_c)
#
#res = float("INF")
#tar_r = (min_r+max_r)//2
#tar_c = (min_c+max_c)//2
#for mr in range(-1, 2, 1):
#    for mc in range(-1, 2, 1):
#        tmp_res = 0
#        tar_rr = tar_r + mr
#        tar_cc = tar_c + mc
#        for r, c in X_lists:
#            move = 0
#            r_r = abs(tar_rr-r)
#            r_c = abs(tar_cc-c)
#            move += min(r_r, r_c)
#            move += abs(r_r-min(r_r, r_c)) + abs(r_c-min(r_r, r_c))
#            tmp_res = max(move, tmp_res)
#
#        res = min(tmp_res, res)
#
#print(res)