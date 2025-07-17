N, M = map(int, input().split())
S_list = input().split() # 取得例：["a", "b", "c"]、1行の入力用
T_list = input().split() # 取得例：["a", "b", "c"]、1行の入力用

t_set = set(T_list)
for s in S_list:
    if s in t_set:
        print("Yes")
    else:
        print("No")