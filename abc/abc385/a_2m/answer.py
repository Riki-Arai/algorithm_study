A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

if len(set(A_list)) == 1:
    print("Yes")
    exit()

for a in A_list:
    tmp_A_list = A_list.copy()
    tmp_A_list.remove(a)
    if sum(tmp_A_list) == a:
        print("Yes")
        exit()

print("No")