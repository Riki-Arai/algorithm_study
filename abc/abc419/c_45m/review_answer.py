def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    n = int(input_data[0])
    x = []
    y = []
    idx = 1
    for _ in range(n):
        xi = int(input_data[idx]); yi = int(input_data[idx + 1])
        x.append(xi)
        y.append(yi)
        idx += 2

    X = max(x) - min(x)
    Y = max(y) - min(y)
    # XとYが独立に動いたとしても斜めに動いたことになることを認知することが大事
    # X>0、Y>0だったとしても最大値の方を減らすことを考えれば、斜めに動くことによって最小の方も勝手に0になってくれるので問題がない
    # Y=0とすると、最大と最小のxの差分を埋めるためにお互いが寄っていくので、所要時間は差分の1/2となる
    # 差分が奇数だった場合は少数点が入り、その場合はどちらかの点がもう一歩進む必要がある
    ans = (max(X, Y) + 1) // 2
    print(ans)


if __name__ == "__main__":
    main()

## first
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