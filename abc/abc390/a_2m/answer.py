A_list = list(map(int, input().split())) # 取得例：[1, 2, 3]、1行の入力用

count = 0
sorted_A_list = sorted(A_list)
for i in range(1, len(A_list)):
    tmp_A_list = A_list.copy()
    tmp_A_list[i] = A_list[i-1]
    tmp_A_list[i-1] = A_list[i]
    if sorted_A_list == tmp_A_list:
        count += 1

if count == 1:
    print("Yes")
else:
    print("No")
