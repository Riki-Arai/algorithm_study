import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1
X_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]
M = int(input()) # 数値：1
S_list = [input() for _ in range(M)] # 取得例：["A","B"・・・"E"]、N行の入力用

l2d_dicts = defaultdict(dict)
for S in S_list:
    i2s_dict = l2d_dicts[len(S)]
    for i, s in enumerate(S, 1):
        if i in i2s_dict:
            i2s_dict[i].add(s)
        else:
            i2s_dict[i] = set(s)
    l2d_dicts[len(S)] = i2s_dict

for S in S_list:
    if len(S) == N:
        for i, s in enumerate(S):
            A, B = X_lists[i]
            if not(A in l2d_dicts and B in l2d_dicts[A] and s in l2d_dicts[A][B]):
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")