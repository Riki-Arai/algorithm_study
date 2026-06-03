from collections import defaultdict

N, M = map(int, input().split())
X_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
c_dict = defaultdict(int)
for _ in range(M):
    C, Y = map(int, input().split())
    c_dict[C-1] = Y