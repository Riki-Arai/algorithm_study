'''
(1) bit全探索を使えれば正解は出せるとは思うが、条件的にTLEになる
(2) 2つ程度の選択をするようなタイプではあるのでDPが良さそう
    →Nと持つべき状態が小さいかどうかをよく確認することが重要
(3) よくよく見るとW*Nの制約が小さめなので、ナップサックの要領でいけるのでは？
(4) 総重量の合計の半分以内にheadの重さを加算しても良いような嬉しさを見つけていく
'''
N = int(input()) # 数値：1

total_w = 0
total_b = 0
inputs_lists = []
for _ in range(N):
    W, H, B = map(int, input().split()) # 取得例：1 2
    total_w += W
    total_b += B
    inputs_lists.append((W, H, B))

thres_w = total_w//2
dp_list = [-float("INF")]*(thres_w+1)
dp_list[0] = total_b
for w, h, b in inputs_lists:
    for j in range(thres_w, w-1, -1):
        if dp_list[j-w] >= 0:
            dp_list[j] = max(dp_list[j-w]-b+h, dp_list[j])

print(max(dp_list))