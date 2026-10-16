#  SortedListは「key=lambda x: -x」で降順にできる。SortedDictはlistやsetの値を持てる、peekitem(bisect_left(1))のイメージで1に近いキーの値を取得可能
from sortedcontainers import SortedList

N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

res = 0
A_list.sort(reverse=True)
s_list = SortedList()
for a in A_list:
    if len(s_list) > 0:
        b_i = s_list.bisect_left(2*a)
        if b_i < len(s_list):
            res += 1
            s_list.discard(s_list[b_i])
        else:
            s_list.add(a)
    else:
        s_list.add(a)

print(res)