A_list = list(map(int, input().split()))
sorted_A_list = sorted(A_list)

for i in range(1, len(A_list)):
    tmp_list = A_list.copy()
    hoge = tmp_list[i-1]
    fuga = tmp_list[i]
    tmp_list[i-1] = fuga
    tmp_list[i] = hoge
    if tmp_list == sorted_A_list:
        print("Yes")
        exit()
print("No")