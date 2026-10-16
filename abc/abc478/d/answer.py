'''
(1) 一度追加をしたらずっとそのままという性質は地味に大切
(2) setのまま考えて素直に処理をするとTLEになってしまう
(3) 区間に関する問題でもあるので、setのことを傍に置いて(1)の視点を意識しながら、区間に関する図を書いてみる
(4) 1~Nごとに重複する区間を排除し、その区間を1ずつ加算をしていけば答えになることに気づく
(5) 遅延セグメント or imosであとは解くだけ
(6) ずっと加算したままという性質がある時はそれを必ず意識する、区間に関する問題は図に書いて考えることが大事
    →1~Nごとの区間で重なっている部分を求める問題に着地することがができた
'''
N, Q = map(int, input().split()) # 取得例：1 2
input_lists = [list(map(int, input().split())) for _ in range(Q)] # 取得例:[[1,2], [3,4]・・[9,10]]、空白区切りの数値入力

max_x = 0
x_set = set()
for _, _, x in input_lists:
    max_x = max(x, max_x)
    x_set.add(x)

x2lrs_lists = [[] for _ in range(max_x+1)]
for l, r, x in input_lists:
    x2lrs_lists[x].append([l, r])

x_list = sorted(list(x_set))
for x in x_list:
    if len(x2lrs_lists[x]) > 1:
        lr_lists = x2lrs_lists[x]
        lr_lists.sort()
        tmp_lrs_lists = [lr_lists[0]]
        for i in range(1, len(lr_lists)):
            if lr_lists[i][0] <= tmp_lrs_lists[-1][1]:
                tmp_lrs_lists[-1][1] = max(lr_lists[i][1], tmp_lrs_lists[-1][1]) 
            else:
                tmp_lrs_lists.append(lr_lists[i])

        x2lrs_lists[x] = tmp_lrs_lists

imos_list = [0]*(N+2)
for lr_lists in x2lrs_lists:
    if len(lr_lists):
        for l, r in lr_lists:
            imos_list[l] += 1
            imos_list[r+1] -= 1

cum_list = [0]
# 両端は番兵なので除外しておく
for x in imos_list[1:-1]:
    cum_list.append(cum_list[-1]+x)

print(*cum_list[1:])