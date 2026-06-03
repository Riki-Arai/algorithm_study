from sortedcontainers import SortedList

N, M = map(int, input().split()) # 取得例：1 2
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

b_list = SortedList(B_list)
res = 0
A_list.sort()
for a in A_list:
    b_i = b_list.bisect_right(2*a)
    if b_i > 0:
        b = b_list[b_i-1]
        b_list.remove(b)
        res += 1

print(res)