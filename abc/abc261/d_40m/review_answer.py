'''
(1) 実装は面倒だとは思うがbit全探索で求めることができそうなところ、それをやってしまうとTLE
(2) NとCの制約が小さいのでCを情報として持てばDPが可能
'''
from collections import defaultdict

N, M = map(int, input().split())
X_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
c2y_dict = defaultdict(int)
for _ in range(M):
    C, Y = map(int, input().split())
    c2y_dict[C] = Y

dp_lists = [[-float("INF")]*(N+1) for _ in range(N+1)]
dp_lists[0][0] = 0
for i in range(1, N+1):
    for j in range(N, 0, -1):
        if j in c2y_dict and dp_lists[i-1][j-1] != float("INF"):
            dp_lists[i][j] = max(dp_lists[i-1][j-1]+X_list[i-1]+c2y_dict[j], dp_lists[i][j])
        elif j not in c2y_dict and dp_lists[j-1] != float("INF"):
            dp_lists[i][j] = max(dp_lists[i-1][j-1]+X_list[i-1], dp_lists[i][j])

        dp_lists[i][0] = max(dp_lists[i-1][j-1], dp_lists[i][0])

print(max(dp_lists[-1]))