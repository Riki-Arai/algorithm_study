N, X, Y = map(int, input().split())
A_list = list(map(int, input().split()))

A_list.sort()
# 最低個数しか持てない子が大きな飴を最大に持てる数を基準
# 上記に該当する数値は減らす意味がないので固定して良い
base_w = A_list[0]*Y
res = sum(A_list)
for a in A_list:
    diff = a*Y - base_w
    dec = Y-X
    if diff%dec != 0:
        print(-1)
        exit()

    # 限界まで減らしてもdiffを0以下にできないのであれば-1
    if diff > dec*a:
        print(-1)
        exit()

    res -= diff//dec

print(res)