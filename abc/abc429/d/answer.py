import sys, bisect as bi
from collections import Counter
sys.setrecursionlimit(10**7)

N, M, C = map(int, input().split())
A_list = list(map(int, input().split()))

c_list = []
i_list = []
for k, v in sorted(Counter(A_list).items()):
    c_list.append(v)
    i_list.append(k)

c_cum_list = [0]
for c in 2 * c_list:
    c_cum_list.append(c_cum_list[-1] + c)

res = 0
for cur_i in range(len(i_list)):
    # 前の人がいる地点から、今の地点までの「円環上の距離」を計算する
    # 例えばcur_i=0の時は0からスタートという意味ではなく、0に位置する人に初めて会う時の状況を想定している
    # そのため下の式ではcur_i-1=-1となるが、これは最後の地点から出発することで最初に0に位置する人に出会うことができる
    dist = (i_list[cur_i] - i_list[cur_i - 1]) % M
    # 距離が0になるのは、人が1箇所にしかいないケース。その場合は1周まるまる(M)が距離となる。
    if dist == 0:
        dist = M
    before = c_cum_list[cur_i]
    b_i = bi.bisect_left(c_cum_list, before+C)
    x = c_cum_list[b_i] - before
    # distに該当する位置は全てxとなるのでまとめて足す
    res += dist * x

print(res)