N, M = map(int, input().split())
A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用
B_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

for b in B_list:
    if b in A_list:
        A_list.remove(b)
    else:
        print("No")
        exit()

print("Yes")