N = int(input()) # 数値：1

thres_w = 0
sum_v = 0
diff_w_lists = []
for _ in range(N):
    W, H, B = map(int, input().split()) # 取得例：1 2
    diff_w_lists.append((W, B-H))
    sum_v += H
    thres_w += W

thres_w = (thres_w+1)//2
dp_list = [-float("INF")]*(500*500+1)
dp_list[0] = sum_v
for w, v in diff_w_lists:
    for i in range(500*500, w-1, -1):
        if dp_list[i-w] >= 0:
            dp_list[i] = max(dp_list[i-w] + v, dp_list[i])
    1
print(max(dp_list[thres_w:]))