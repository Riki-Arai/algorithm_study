import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1
S_list = [input().strip() for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]、文字列をリストに分解

max_l = max(map(len, S_list))
s2l_dict = defaultdict(int)
for j in range(max_l):
    a2list_dicts = defaultdict(list)
    for i in range(N):
        if S_list[i] not in s2l_dict and j < len(S_list[i]):
            a2list_dicts[S_list[i][j]].append(S_list[i])
        elif S_list[i] not in s2l_dict and j == len(S_list[i]):
            s2l_dict[S_list[i]] = j

    for k, v in a2list_dicts.items():
        if len(v) < 2:
            for s in v:
                s2l_dict[s] = j

for s in S_list:
    if s not in s2l_dict:
        print(len(s))
    else:
        print(s2l_dict[s])