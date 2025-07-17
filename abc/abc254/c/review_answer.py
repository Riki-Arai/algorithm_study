# クイックソートなどを実装しないとダメかと思ったが、理解すると単純な問題であった
# 結局入れ替えを何回かやればソートした順番になるので、それならば最初からsortを使えば良いという発想
N, K = map(int, input().split())
A_list = list(map(int, input().split()))

res_list = [None] * N
for i in range(K):
    # i番目を起点としてK個飛ばしで値を取得してソート
    res_list[i::K] = sorted(A_list[i::K])

A_list.sort()
if res_list == A_list:
    print("Yes")
else:
    print("No")