'''
(1) 解説でもあったが数列で三つの値を扱うときは真ん中に着目するといい
(2) 右側と左側で辞書を持っておき、右にずらしながら値を更新していけば解ける
'''
from collections import defaultdict, Counter

N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

ra2c_dict = Counter(A_list)
la2c_dict = defaultdict(int)
res = 0
sum_ = 0
l_n, r_n = 0, N
for a in A_list:
    res += sum_-la2c_dict[a]*ra2c_dict[a]
    sum_ -= la2c_dict[a]*ra2c_dict[a]
    l_n += 1
    la2c_dict[a] += 1
    r_n -= 1
    ra2c_dict[a] -= 1
    sum_ += la2c_dict[a]*ra2c_dict[a]

print(res)