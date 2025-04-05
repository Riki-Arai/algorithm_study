N = int(input())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

res = 0
c_set = set(A_list) & set(B_list)
for i in c_set:
    if A_list.index(i) == B_list.index(i):
        res += 1
print(res)
print(len(c_set)-res)