'''
(1) 双方向リストとはすぐにわかったが実装に意外と時間がかかった
    →処理がごちゃつくタイプの実装が遅い
    →図に書いて整理をした上でコードで表現する癖をつけたい
(2) 番兵を設けることが案外重要
'''
from collections import defaultdict

N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
Q = int(input()) # 数値：1

f2b_dict, b2f_dict = defaultdict(int), defaultdict(int)
f2b_dict[0] = A_list[0]
b2f_dict[-1] = A_list[-1]
for i in range(N-1):
    f2b_dict[A_list[i]] = A_list[i+1]
    b2f_dict[A_list[i+1]] = A_list[i]

for _ in range(Q):
    input_ = input().split()
    if input_[0] == "1":
        x, y = int(input_[1]), int(input_[2])
        b = f2b_dict[x]
        f2b_dict[x] = y
        f2b_dict[y] = b
        b2f_dict[b] = y
        b2f_dict[y] = x
    else:
        x = int(input_[1])
        b = f2b_dict[x]
        f = b2f_dict[x]
        f2b_dict[f] = b
        b2f_dict[b] = f
        del f2b_dict[x], b2f_dict[x]

res_list = []
i = 0
while f2b_dict[i] != 0:
    i = f2b_dict[i]
    res_list.append(i)

print(*res_list)