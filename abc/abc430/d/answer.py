from sortedcontainers import SortedList
from collections import defaultdict

N = int(input())
X_list = list(map(int, input().split()))

res = 0
x2d_dict = defaultdict(lambda: float("INF"))
s_list = SortedList([0])

def g(x, d):
    if x2d_dict[x] == float("INF"):
        x2d_dict[x] = d
        return d
    elif x2d_dict[x] > d:
        diff = d - x2d_dict[x]
        x2d_dict[x] = d
        return diff
    return 0


for x in X_list:
    s_list.add(x)
    b_i = s_list.bisect_left(x)

    # 左隣の人の更新
    if b_i > 0:
        res += g(s_list[b_i - 1], x - s_list[b_i - 1])

    # 右隣の人の更新
    if b_i + 1 < len(s_list):
        res += g(s_list[b_i + 1], s_list[b_i + 1] - x)

    # 新しく来た人の更新
    d = float("INF")
    if b_i > 0:
        d = min(d, x - s_list[b_i - 1])
    if b_i + 1 < len(s_list):
        d = min(d, s_list[b_i + 1] - x)

    res += g(x, d)

    print(res)