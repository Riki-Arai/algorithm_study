# A_listを変換して二部探索を扱えるようにする
# pythonのbisectで扱えるように-1倍すれば昇順になる
# b_listについても-1をする必要あり

import bisect

# 入力部分を置き換え
N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

# A_list[i+1] = min(A_list[i+1], A_list[i]) により
# 左から右への非増(降順)になるよう整形
for i in range(N - 1):
    if A_list[i + 1] > A_list[i]:
        A_list[i + 1] = A_list[i]

# Python の bisect は昇順想定なので、値を -1 倍した配列を作る
negative_a = []
for x in A_list:
    negative_a.append(-x)

# B_list の各要素に対して、A_list 内で
# 「A_list[i] <= B_list[j] となる最初の位置 i」を探す
# (降順データに対応するよう negative_a で bisect_left(-val) を実行)
for val in B_list:
    pos = bisect.bisect_left(negative_a, -val)
    if pos == N:
        print(-1)
    else:
        print(pos + 1)