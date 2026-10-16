'''
(1) HとWの制約が小さいのでDPやUFを考えたがいずれもTLEになってしまう(そもそもグラフでDPを使うパターンは少ない)
(2) 取り込んだスライムを毎回探索することも考えたが、制約が小さいとはいえい複が発生するのでTLEになりそう
(3) 視点を変更してて周辺に着目し、そこでひとまず取り込んでしまい処理ができそうなものから順番に処理をすることお思いつく
(4) 取り込んだマスをsetで管理をして、一度だけチェックをする仕組みで処理をすれば間に合う
(5) 図をとにかく書きまくって検証、視点を変更をしてみる重要性を再認識した
    →周辺の情報をひとまず取り込むという考え方は今後も使えそう
'''
import heapq as hq

H, W, X = map(int, input().split()) # 取得例：1 2
P, Q = map(int, input().split()) # 取得例：1 2
input_lists = [list(map(int, input().split())) for _ in range(H)] # 取得例:[[1,2], [3,4]・・[9,10]]、空白区切りの数値入力

P -= 1
Q -= 1
hq_lists = []
seen_sets = set([(P, Q)])
move_lists = {"L":(-1, 0), "U":(0, -1), "R":(1, 0), "D":(0, 1)}.values()
res = input_lists[P][Q]
for mi, mj in move_lists:
    i = P+mi
    j = Q+mj
    if 0 <= i < H and 0 <= j < W and (i, j) not in seen_sets:
        seen_sets.add((i, j))
        hq.heappush(hq_lists, (input_lists[i][j]*X+1, input_lists[i][j], i, j))

while len(hq_lists):
    c, s, b_i, b_j = hq.heappop(hq_lists)
    if c <= res:
        res += s
        for mi, mj in move_lists:
            i = b_i+mi
            j = b_j+mj
            if 0 <= i < H and 0 <= j < W and (i, j) not in seen_sets:
                seen_sets.add((i, j))
                hq.heappush(hq_lists, (input_lists[i][j]*X+1, input_lists[i][j], i, j))
    else:
        break

print(res)