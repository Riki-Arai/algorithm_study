from collections import defaultdict

N = int(input()) # 数値：1
input_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]、空白区切りの数値入力
Q = int(input()) # 数値：1
T_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

max_h = []
l2h_dict = defaultdict(int)
for h, l in input_lists:
    l2h_dict[l] = max(l2h_dict[l], h)

l2h_lists = sorted(list(l2h_dict.items()))
l_list, mh_list = [], []
for l, h in l2h_lists:
    l_list.append(l)
    if h == max_h:
        mh_list.append(h)